from playwright.sync_api import Page

class BasketPage:

    QUANTITY_DROPDOWN  = ".a-button-text.a-declarative"
    QUANTITY_OPTION    = "a[tabindex='-1']#quantity_"
    QUANTITY_SELECTED  = ".a-dropdown-prompt"
    PRICE_PER_ITEM     = ".a-color-base.a-size-medium.a-text-bold.sc-price.sc-product-price.sc-white-space-nowrap"
    ACTUAL_TOTAL_PRICE = "span[id*='sc-subtotal-amount']"

    def __init__(self, page: Page):
        self.page = page

    def update_quantity(self, desired_quantity):
        self.page.click(self.QUANTITY_DROPDOWN)
        self.page.wait_for_load_state()
        self.page.click(self.QUANTITY_OPTION + str(desired_quantity))
        self.page.wait_for_timeout(2000)        

    # function to get the quantity displayed after the user updated the quantity
    def get_quantity(self) -> float:
        return float(self.page.inner_text(self.QUANTITY_SELECTED))

    def get_item_price(self) -> float:
        self.page.wait_for_load_state()
        item_price_text = self.page.inner_text(self.PRICE_PER_ITEM)
        return float(item_price_text.replace('€', '').replace(',', '').strip())
    
    def get_total_price(self) -> float:
        self.page.wait_for_load_state()
        total_price_text = self.page.inner_text(self.ACTUAL_TOTAL_PRICE)
        return float(total_price_text.replace('€', '').replace(',', '').strip())
    
    def calculate_expected_price(self) ->int:
        quantity = self.get_quantity()
        price_per_item = self.get_item_price()
        return quantity*price_per_item