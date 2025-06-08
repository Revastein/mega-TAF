from functools import cached_property

from components.cart_page.cart_page import CartPage
from components.catalog_page.catalog_page import CatalogPage
from components.favorite_page.favorite_page import FavoritePage
from components.main_page.main_page import MainPage


class Site:
    def __init__(self, driver):
        self.driver = driver

    @cached_property
    def main_page(self) -> MainPage:
        return MainPage(self.driver)

    @cached_property
    def catalog_page(self) -> CatalogPage:
        return CatalogPage(self.driver)

    @cached_property
    def cart_page(self) -> CartPage:
        return CartPage(self.driver)

    @cached_property
    def favorite_page(self) -> FavoritePage:
        return FavoritePage(self.driver)
