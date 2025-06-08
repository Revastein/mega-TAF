from typing import Any, Callable

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10


class WaitUntil(WebDriverWait):
    def __init__(self, driver: WebDriver, timeout: float = DEFAULT_TIMEOUT):
        super().__init__(driver, timeout)

    def safe_until(self, condition: Callable, message: str | None = None) -> Any:
        try:
            return self.until(condition, message=message)
        except TimeoutException:
            return False

    def safe_until_not(self, condition: Callable, message: str | None = None) -> Any:
        try:
            return self.until_not(condition, message=message)
        except TimeoutException:
            return False
