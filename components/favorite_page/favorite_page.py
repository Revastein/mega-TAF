from base.base_page import BasePage
from components.config import FAVORITE_PAGE_URL
from helpers.locators import BaseLocator


class FavoritePage(BasePage, BaseLocator):
    def __init__(self, driver):
        super().__init__(driver, page_url=FAVORITE_PAGE_URL)
        self.page_title = self.by_locator("css", '[class="mb-md-5 mb-4"]')
        self.product_item = self.by_locator("css", "[class~=rs-product-item]")
        self.product_title = self.by_locator("css", '[class~="item-card__title"]')
        self.remove_from_favorite = self.by_locator("css", "[class~=rs-favorite]")
