from helpers.locators import BaseLocator


class CatalogDropdown(BaseLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.category_electronics = self.by_locator("link_text", "Электроника")
        self.subcategory_tablets = self.by_locator("link_text", "Планшеты")
        self.brand_digma = self.by_locator("link_text", "Digma")
