"""
This module will be like a template for other modules to reduce code duplicate
Will have at least(I guess) page object, navigation method, andd generic interaction methods: click(locator), fill(locator)
BasePage should have common functionalities that other classes can inherit to use:
-> Start the browser
-> Headless Mode support
-> Implicit Waits 
"""

"""
BasePage class should
->  Launch the browser only once and create a page object.
-> Provide reusable actions (e.g., goto(), click(), fill()).
-> Not close the browser immediately, so tests can run.
"""

from playwright.sync_api import Page
# from utils.browser_manager import page_instance

class BasePage:
    def __init__(self, page: Page):
        self.page = page    

    # define a goto method
    def access_url(self, url):
        self.page.goto(url)

    # method for getting a locator
    def get_locator(self, selector):
        return self.page.locator(selector)
    
    # click on a locator
    def detailed_click(self, selector):
        print(f"Clicking on {selector}")
        element = self.get_locator(selector)
        element.wait_for()
        element.click()

    # to fill an input
    def fill_locator(self, selector, text):
        self.get_locator(selector).fill(text)

    # wait 5 seconds
    def wait_for_element(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)


        

