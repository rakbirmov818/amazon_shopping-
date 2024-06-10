from playwright.sync_api import Page

class ProductPage:

    ADD_TO_BASKET_BTN = "#a-autoid-1"
    GO_TO_BASKET_BTN  = "#nav-cart-count-container"

    def __init__(self, page: Page):
        self.page = page

    def add_to_basket(self):
        self.page.click(self.ADD_TO_BASKET_BTN)
        self.page.wait_for_selector(self.ADD_TO_BASKET_BTN).is_visible

    def navigate_to_basket(self):
        self.page.wait_for_selector(self.GO_TO_BASKET_BTN).click() 