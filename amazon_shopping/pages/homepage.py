from playwright.sync_api import Page

class HomePage:

    URL            = "https://www.amazon.de/-/en/ref=nav_logo"
    ACCEPT_COOKIES = "input#sp-cc-accept"
    CLOSE_TOASTER  = ".glow-toaster-button-dismiss .a-button-input"
    SEARCH_FIELD   = "#twotabsearchtextbox"
    SEARCH_BTN     = "[value='Go']"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        self.page.wait_for_selector(self.ACCEPT_COOKIES).click()
        self.page.wait_for_selector(self.CLOSE_TOASTER).click()
          
    def search_product(self, product_name: str):
        self.page.fill(self.SEARCH_FIELD, product_name)
        self.page.click(self.SEARCH_BTN)