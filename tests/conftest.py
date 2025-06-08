import os
import shlex

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.site_entry import Site
from components.config import chrome_options

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--username",
        default=os.getenv("TEST_USERNAME", "test.test@test.test"),
        help="user login (fallback stub)",
    )
    parser.addoption(
        "--password",
        default=os.getenv("TEST_PASSWORD", "stub_password"),
        help="user pass (fallback stub)",
    )
    parser.addoption(
        "--chrome-options",
        default=" ".join(chrome_options),
        help='all Chrome CLI flags, space-separated, e.g. "--headless=new --window-size=1280,720"',
    )


@pytest.fixture(scope="session")
def credentials(request):
    return {
        "username": request.config.getoption("username"),
        "password": request.config.getoption("password"),
    }


@pytest.fixture
def chrome_driver(request):
    opts = Options()
    chrome_opts = request.config.getoption("chrome_options")

    for arg in shlex.split(chrome_opts):
        opts.add_argument(arg)

    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


@pytest.fixture
def site(chrome_driver):
    return Site(chrome_driver)
