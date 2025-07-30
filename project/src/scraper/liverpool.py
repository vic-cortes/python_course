from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base import BaseScraper
from .utils import normalize_string

BASE_URL = "https://www.liverpool.com.mx"
PRODUCT_URL = f"{BASE_URL}/tienda?s=lavadoras"


@dataclass
class ParentScraper(BaseScraper):
    driver: webdriver.Firefox

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
        self._ensure_key_product_tags_exists("m-product__card")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        product_items = soup.select("li.m-product__card")

        product_links = []

        for item in product_items:
            product_tag = ParentProductTag(item)
            full_link = f"{BASE_URL}{product_tag.href}"
            product_links.append(full_link)

        print(f"Found {len(product_links)} product links.")

        return product_links


@dataclass
class ParentProductTag:
    node: Tag

    @property
    def href(self) -> str:
        return self.node.find("a")["href"]

    def get_all_article_info_node(self) -> Tag:
        return self.node.find("figcaption")


@dataclass
class DetailScraper(BaseScraper):
    driver: webdriver.Firefox
    detail_url: str
    KEY_PRODUCT_TAG = "o-product__productSpecsList"

    def __post_init__(self):
        self.driver.get(self.detail_url)
        self._ensure_key_product_tags_exists(self.KEY_PRODUCT_TAG, by_type=By.CLASS_NAME, timeout=10)
        self._soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def get_price(self) -> str:
        return {}

    def get_product_details(self) -> dict:
        """
        Get product details from a given product URL.
        """
        # Retrieve tags from specifications
        tag_product_spec_titles = self._soup.find_all(
            "span", class_="productSpecsGrouped_bold"
        )
        tag_product_specs = self._soup.find_all("span", class_="productSpecsGrouped_regular")

        # Retrieve text from tags and normalize it
        product_spec_titles = [
            normalize_string(el.text) for el in tag_product_spec_titles
        ]
        product_spec = [el.text for el in tag_product_specs]

        # Create a dictionary with product specifications
        product_specs = dict(zip(product_spec_titles, product_spec))

        return product_specs
    
    def get_all_data(self) -> dict:
        """
        Get all data from the product detail page.
        """
        final_data = {}
        final_data["specs"] = self.get_product_details()
        final_data["price"] = self.get_price()

        return final_data
