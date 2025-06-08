import traceback
from contextlib import contextmanager
from typing import Any, Callable

from helpers.allure import attach_screenshot

import allure


class Expected:
    def __init__(self, driver):
        self.driver = driver
        self.condition = None
        self.error_msg = None
        self.include_screenshot = True

    @contextmanager
    def step(self, step_name: str, include_screenshot=True):
        self.include_screenshot = include_screenshot
        try:
            with allure.step(step_name):
                yield self
                if self.condition is not None and not self.condition():
                    msg = (
                        self.error_msg()
                        if callable(self.error_msg)
                        else self.error_msg or "Condition failed"
                    )
                    if self.include_screenshot:
                        attach_screenshot(self.driver, "Failure screenshot")
                    raise AssertionError(msg)
        except Exception:
            if self.include_screenshot:
                attach_screenshot(self.driver, "Exception screenshot")
            tb = traceback.format_exc()
            allure.attach(
                tb, name="Traceback", attachment_type=allure.attachment_type.TEXT
            )
            raise

    def is_equal(self, current: Any, expected: Any):
        self.condition = lambda: current == expected
        self.error_msg = lambda: f'Actual result "{current}", expected "{expected}"'

    def wait_for(self, condition: Callable, timeout=5, poll=0.2):
        from time import time, sleep

        start = time()
        while time() - start < timeout:
            if condition():
                self.condition = lambda: True
                self.error_msg = ""
                return
            sleep(poll)
        self.condition = lambda: False
        self.error_msg = f"Timeout {timeout}s waiting for condition"
