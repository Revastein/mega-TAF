from helpers.locators import BaseLocator


class CartForm(BaseLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_title = self.by_locator("css", '[class="modal-cart-item__title"]')
        self.go_to_cart_button = self.by_locator("link_text", "Перейти в корзину")
