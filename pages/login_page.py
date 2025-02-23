from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # inherit BasePage methods

    # to get back here
    def login(self,username, password, sign_in_button):
        self.fill_locator("[name='username']", username)
        self.fill_locator("[name='password']", password)
        self.click(sign_in_button)

    # def login(self,username, password):
    #     self.click("menuUserLink")
    #     self.fill_locator("[name='username']", username)
    #     self.fill_locator("[name='password']", password)
    #     self.click("#sign-in-button")


