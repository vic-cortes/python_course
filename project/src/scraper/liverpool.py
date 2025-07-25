import os

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .constants import GECKO_DRIVER_PATH
from .utils import get_firefox_driver

BASE_URL = "https://www.liverpool.com.mx/tienda?s=lavadoras"
STRATEGY = "none"


def get_product_links(driver: webdriver.Firefox) -> list[str]:
    """
    Get product links from the Liverpool website.
    """
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-item"))
        )
    except TimeoutException:
        print("Timeout while waiting for product items to load.")
        return []

    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_items = soup.select("div.product-item")

    product_links = []
    for item in product_items:
        link_tag = item.select_one("a.product-item-link")
        if link_tag and isinstance(link_tag, Tag):
            product_links.append(link_tag["href"])

    return product_links


if __name__ == "__main__":
    driver = get_firefox_driver()
    product_links = get_product_links(driver)
    print(product_links)
    driver.quit()
