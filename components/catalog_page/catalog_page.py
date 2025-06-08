from base.base_page import BasePage
from components.config import CATALOG_PAGE_URL
from helpers.locators import BaseLocator


class CatalogPage(BasePage, BaseLocator):
    def __init__(self, driver):
        super().__init__(driver, page_url=CATALOG_PAGE_URL)
        self.page_title = self.by_locator("tag_name", "h1")
        self.product_titles = self.by_locator("css", '[class~="item-card__title"]')
