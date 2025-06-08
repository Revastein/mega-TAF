from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_con

from helpers.waits import WaitUntil


class LocatorWrapper:
    def __init__(self, driver, by, locator):
        self.driver = driver
        self.by = by
        self.locator = locator

    def find(self):
        return WaitUntil(self.driver).safe_until(
            ex_con.visibility_of_element_located((self.by, self.locator)),
            message=f"Can't find element by {self.by}='{self.locator}'",
        )

    def find_all(self):
        return self.driver.find_elements(self.by, self.locator)

    def click(self):
        return self.find().click()

    def text(self):
        return self.find().text

    def send_keys(self, value):
        return self.find().send_keys(value)

    def get_attribute(self, attr):
        return self.find().get_attribute(attr)

    def value(self) -> str:
        return self.find().get_attribute("value")

    def int_value(self) -> int:
        return int(self.value())

    def clear_and_send_value(self, value):
        self.find().clear()
        self.find().send_keys(value)

    def move_to_element(self):
        element = self.find()
        ActionChains(self.driver).move_to_element(element).perform()
        return self


class BaseLocator:
    def __init__(self, driver):
        self.driver = driver

    def by_locator(self, by: str, locator: str) -> LocatorWrapper:
        by_value = self._get_element_by(by)
        return LocatorWrapper(self.driver, by_value, locator)

    @staticmethod
    def _get_element_by(find_by: str) -> str:
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT,
            "name": By.NAME,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag_name": By.TAG_NAME,
        }
        return locating[find_by]
