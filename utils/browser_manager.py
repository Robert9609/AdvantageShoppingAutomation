from playwright.sync_api import sync_playwright, Playwright

class BrowserManager:
    def __init__(self, headless: bool = True):
        #Initialize Playwright objects like browser, page and playwright
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
    
    def close_browser(self):
        self.browser.close()
        self.playwright.stop()
    


