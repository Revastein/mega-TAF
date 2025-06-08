import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ex_con

from helpers.expected import Expected
from helpers.waits import WaitUntil


class BasePage:
    def __init__(self, driver: WebDriver, page_url: str = ""):
        self.driver = driver
        self.page_url = page_url
        self.wait = WaitUntil(driver)
        self.expected = Expected(driver)

    def is_opened(self):
        with allure.step(f"Page {self.page_url} is opened"):
            return self.wait.safe_until(ex_con.url_to_be(self.page_url))

    def go_to_page(self):
        with allure.step(f"Open {self.page_url} page"):
            self.driver.get(self.page_url)
        self.is_opened()
