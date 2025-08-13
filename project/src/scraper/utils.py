import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from ..scraper.constants import GECKO_DRIVER_PATH

STRATEGY = "none"


def normalize_string(raw_string: str) -> str:
    """
    Remove accents from a given string and convert it to lowercase.
    """
    if raw_string is None:
        raise ValueError("Input string cannot be None")

    ACCENTS = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ñ": "n",
        "ü": "u",
    }
    raw_string = "_".join(raw_string.split()).lower()

    for accent, replacement in ACCENTS.items():
        raw_string = raw_string.replace(accent, replacement)

    return raw_string


def get_firefox_driver(headless: bool = False) -> webdriver.Firefox:
    """
    Get a Firefox WebDriver instance.
    """
    options = Options()

    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    options.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/110.0",
    )
    options.set_capability("pageLoadStrategy", STRATEGY)
    capabilities = DesiredCapabilities.FIREFOX
    capabilities["pageLoadStrategy"] = STRATEGY
    # capabilities["marionette"] = True

    service = Service(executable_path=GECKO_DRIVER_PATH, log_output=os.path.devnull)
    driver = webdriver.Firefox(service=service, options=options)

    return driver
