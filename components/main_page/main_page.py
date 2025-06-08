from base.base_page import BasePage
from components.cart_page.cart_form import CartForm
from components.config import MAIN_PAGE_URL
from components.main_page.catalog_dropdown import CatalogDropdown
from components.main_page.login_form import LoginForm
from helpers.locators import BaseLocator


class MainPage(BasePage, BaseLocator):
    def __init__(self, driver):
        super().__init__(driver, page_url=MAIN_PAGE_URL)
        self.login_form = LoginForm(driver)
        self.catalog_dropdown = CatalogDropdown(driver)
        self.cart_form = CartForm(driver)

        self.login_dropdown = self.by_locator("css", '[data-bs-toggle="dropdown"]')
        self.login_button = self.by_locator("link_text", "Вход")

        self.catalog_button = self.by_locator("css", "[class~=dropdown-catalog-btn]")

        self.product_card_title = self.by_locator("css", '[class~="item-card__title"]')
        self.add_to_cart_button = self.by_locator(
            "css", "[class=item-product-cart-action]"
        )

        self.add_to_favorite = self.by_locator("css", "[class~=rs-favorite]")
        self.go_to_favorite_page_button = self.by_locator(
            "css", "[class~=rs-favorite-block]"
        )
