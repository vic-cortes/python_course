from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .utils import normalize_string

BASE_URL = "https://www.liverpool.com.mx"
PRODUCT_URL = f"{BASE_URL}/tienda?s=lavadoras"


@dataclass
class LiverpoolScraper:
    driver: webdriver.Firefox

    def _ensure_key_product_tags_exists(self) -> None:
        """
        Wait until a product tag is present on the page.
        """
        TIMEOUT = 5  # seconds
        # wait until a tag with class exists
        try:
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, "m-product__card"))
            )
        except (TimeoutException, NoSuchElementException):
            raise ValueError("Product tag not found or not loaded properly.")

    def product_node(self, item: Tag) -> str:
        """
        Extract product link from a product item.
        """
        try:
            link_tag = item.select_one("a.product-item-link")
            if link_tag and isinstance(link_tag, Tag):
                return link_tag["href"]
            return ""
        except NoSuchElementException:
            return ""

    def get_product_links(self) -> list[str]:
        """
        Get product links from the Liverpool website.
        """
        self.driver.get(PRODUCT_URL)
        self._ensure_key_product_tags_exists()

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        product_items = soup.select("li.m-product__card")

        product_links = []

        for item in product_items:
            product_tag = LiverpoolParentProductTag(item)
            full_link = f"{BASE_URL}{product_tag.href}"
            product_links.append(full_link)

        print(f"Found {len(product_links)} product links.")

        return product_links


@dataclass
class LiverpoolParentProductTag:
    node: Tag

    @property
    def href(self) -> str:
        return self.node.find("a")["href"]

    def get_all_article_info_node(self) -> Tag:
        return self.node.find("figcaption")


@dataclass
class LiverpoolDetailScraper:
    driver: webdriver.Firefox
    detail_url: str

    def _ensure_key_product_tags_exists(self) -> None:
        """
        Wait until a product tag is present on the page.
        """
        TIMEOUT = 10  # seconds
        # wait until a tag with class exists
        try:
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "o-product__productSpecsList")
                )
            )
        except (TimeoutException, NoSuchElementException):
            raise ValueError("Product tag not found or not loaded properly.")

    def get_product_details(self) -> dict:
        """
        Get product details from a given product URL.
        """
        self.driver.get(self.detail_url)

        self._ensure_key_product_tags_exists()
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        # Retrieve tags from specifications
        tag_product_spec_titles = soup.find_all(
            "span", class_="productSpecsGrouped_bold"
        )
        tag_product_specs = soup.find_all("span", class_="productSpecsGrouped_regular")

        # Retrieve text from tags and normalize it
        product_spec_titles = [
            normalize_string(el.text) for el in tag_product_spec_titles
        ]
        product_spec = [el.text for el in tag_product_specs]

        # Create a dictionary with product specifications
        product_specs = dict(zip(product_spec_titles, product_spec))

        return product_specs
