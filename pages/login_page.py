from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # inherit BasePage methods

    # to get back here
    def login(self,username, password):
        self.fill_locator("[name='username']", username)
        self.fill_locator("[name='password']", password)



