from helpers.locators import BaseLocator


class LoginForm(BaseLocator):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_field = self.by_locator("css", '[name="login"]')
        self.password_field = self.by_locator("css", '[name="pass"]')
        self.submit_button = self.by_locator("css", '[type="submit"].btn')
