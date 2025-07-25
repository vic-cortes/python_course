import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from .constants import GECKO_DRIVER_PATH

BASE_URL = "https://www.liverpool.com.mx/tienda?s=lavadoras"
STRATEGY = "none"


def get_firefox_driver() -> webdriver.Firefox:
    """ "
    Get a Firefox WebDriver instance.
    """
    options = Options()
    options.headless = False
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities["marionette"] = True

    service = Service(executable_path=GECKO_DRIVER_PATH, log_output=os.path.devnull)
    driver = webdriver.Firefox(
        service=service,
        options=options,
        desired_capabilities=capabilities,
    )

    return driver
