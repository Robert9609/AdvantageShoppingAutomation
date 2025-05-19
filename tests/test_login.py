# Successfull Login test


"""
This test shoul'd access an endpoint, interact with username and password fields, fill them and then select Log In button
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import time
from pages.login_page import LoginPage
from utils.browser_manager import BrowserManager


def test_login():
    # Execute the init inside BrowserManager class which starts playwright and a browser
    setup_initializer = BrowserManager(headless=True)
    print("Playwright started, browser launched")

    # Create a new page(this is just a simple page)
    page_object = setup_initializer.browser.new_page()

    # pass the page(page_object) to LoginPage class
    login_page = LoginPage(page_object)

    # Access the url
    login_page.access_url("https://www.advantageonlineshopping.com/#/")

    # Apply a waiter(also used default page object again because our base_page that we passed to LoginPage is a basePage object and doesn't have the wait_for_load_state method)
    login_page.page.wait_for_load_state("networkidle")
    
    # Here I use get_locator method, I pass a selector and create a locator to access the login button and then perform click on it
    login_page.get_locator("#menuUserLink").click()    # Why here I cannot call my detailed_click() method?

    login_page.wait_for_element("#menuUserLink")

    # Wait about 2 seconds to be sure the login popul is loaded because I noticed it took about 1 second to appear
    time.sleep(5)
    
    #Log in button

    login_page.login(username="testacc1", password="Pass1234#")

    # Sleep after credentials are entered and click on the sign in button
    time.sleep(5)

    locator = login_page.get_locator("#sign_in_btn")
    locator.wait_for(state="visible")
    
    locator.click()

    time.sleep(3)

    # close the browser after the test finish

    setup_initializer.close_browser()