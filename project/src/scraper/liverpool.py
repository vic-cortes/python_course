from __future__ import annotations

import random
import time
from dataclasses import dataclass

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By

from .base import BaseScraper
from .utils import normalize_string

BASE_URL = "https://www.liverpool.com.mx"
PRODUCT_URL = f"{BASE_URL}/tienda?s=lavadoras"


@dataclass
class ParentScraper(BaseScraper):
    driver: webdriver.Firefox

    @property
    def service_name(self) -> str:
        return "liverpool"

    def go_to_main_page(self) -> None:
        """
        Navigate to the Liverpool home page.
        """
        self.driver.get(PRODUCT_URL)

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

    def _click_next_page(self) -> bool:
        """
        Click the "next page" button to load more products.
        """
        CSS_SELECTOR = "li.page-item:nth-child(8) > a:nth-child(1)"

        try:
            self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR).click()
            success = True
        except ElementNotInteractableException:
            success = False
        except Exception as e:
            print(f"Error clicking next page: {e}")
            success = False
        finally:
            return success

    def get_all_links(self) -> list[str]:
        """
        Get all product links from the Liverpool website.
        """
        self.go_to_main_page()

        # Product links from the first page
        product_links = self.get_product_links()

        while self._click_next_page():
            new_product_links = self.get_product_links()
            product_links.extend(new_product_links)

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
    # KEY_PRODUCT_TAG = "o-product__productSpecsList"
    KEY_PRODUCT_TAG = "productSpecsGrouped_bold"

    def __post_init__(self):
        print(f"* Scraping product details from: {self.detail_url}")
        self.driver.get(self.detail_url)
        self._ensure_key_product_tags_exists(self.KEY_PRODUCT_TAG, timeout=10)
        # Wait randomly for the page to load to prevent being blocked
        # by the website for making too many requests in a short time
        time.sleep(random.uniform(1, 3))
        self._soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def get_price(self) -> str:
        JUST_ONE_PRICE = 1
        KEY_PRICE_NAME = "DiscountPrice"

        price_node = self._soup.find("div", class_="m-product__price--collection")

        prices = []

        for node_p in price_node.find_all("p"):
            node_class = "__".join(node_p["class"])

            if KEY_PRICE_NAME in node_class:
                prices.append(node_p.text.strip())

        if len(prices) != JUST_ONE_PRICE:
            raise ValueError("Price not found on the page.")

        raw_price = prices[0]
        string_price = [el for el in list(raw_price) if el.isdigit()]
        return float("".join(string_price)) / 100

    def get_product_details(self) -> dict:
        """
        Get product details from a given product URL.
        """
        # Retrieve tags from specifications
        tag_product_spec_titles = self._soup.find_all(
            "span", class_="productSpecsGrouped_bold"
        )
        tag_product_specs = self._soup.find_all(
            "span", class_="productSpecsGrouped_regular"
        )

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
