from base.base_page import BasePage
from components.config import CART_PAGE_URL
from helpers.locators import BaseLocator


class CartPage(BasePage, BaseLocator):
    def __init__(self, driver):
        super().__init__(driver, page_url=CART_PAGE_URL)
        self.page_title = self.by_locator("css", '[class="h1"]')
        self.added_items = self.by_locator("css", "[data-uniq]")
        self.product_count = self.by_locator("css", "[data-uniq] .rs-amount")
        self.product_titles = self.by_locator(
            "css", '[class="cart-checkout-item__title"]'
        )
        self.remove_button = self.by_locator("css", "[class~=rs-remove]")
        self.submit_order_button = self.by_locator(
            "css", "[class~=rs-checkout_submitButton]"
        )
        self.electronic_delivery_button = self.by_locator("css", '[for="dlv_5"]')
