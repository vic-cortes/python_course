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

BASE_URL = "https://www.elpalaciodehierro.com"
PRODUCT_URL = f"{BASE_URL}/buscar?q=lavadoras"


@dataclass
class ParentScraper(BaseScraper):
    driver: webdriver.Firefox

    @property
    def service_name(self) -> str:
        return "Palacio de hierro"

    def go_to_main_page(self) -> None:
        """
        Navigate to the Palacio de hierro home page.
        """
        self.driver.get(PRODUCT_URL)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for the page to load

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
        Get product links from the Palacio de hierro website.
        """
        self._ensure_key_product_tags_exists("article.m-product", By.CSS_SELECTOR)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        ## with open("pagina.html", "w", encoding="utf-8") as f:
            ##f.write(soup.prettify())

        product_items = soup.select("div.b-product")

        product_links = []

        for item in product_items:
            product_tag = ParentProductTag(item)
            full_link = product_tag.href
            product_links.append(full_link)

        print(f"Found {len(product_links)} product links.")

        return product_links

    def _click_next_page(self) -> bool:
        """
        Click the "next page" button to load more products.
        """
        CSS_SELECTOR = "li.b-next-btn"

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
        Get all product links from the Palacio de hierro website.
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
    KEY_PRODUCT_TAG = "l-pdp-description"

    def __post_init__(self):
        print(f"* Scraping product details from: {self.detail_url}")
        self.driver.get(self.detail_url)
        self._ensure_key_product_tags_exists(self.KEY_PRODUCT_TAG, timeout=10)

        # Wait randomly for the page to load to prevent being blocked
        # by the website for making too many requests in a short time
        time.sleep(random.uniform(1, 3))
        self._soup = BeautifulSoup(self.driver.page_source, "html.parser")
        
        with open("pagina_detalle.html", "w", encoding="utf-8") as f:
            f.write(self._soup.prettify())
        
    def get_price(self) -> str:
        JUST_ONE_PRICE = 1
        KEY_PRICE_NAME = "b-product_price-value"
        
        try:
            price_node = self._soup.find("div", class_="b-product_price-sales")
            
            prices = []

            for node_p in price_node.find_all("span"):
                node_class = node_p.get('class')
                
                if KEY_PRICE_NAME in node_class:
                    prices.append(node_p.text.strip())

            if len(prices) != JUST_ONE_PRICE:
                raise ValueError("Price not found on the page.")

            raw_price = prices[0]
            string_price = [el for el in list(raw_price) if el.isdigit()]
            return float("".join(string_price)) / 100
        except Exception as e:
            print(f'error while retrieving price: {e}')

    def get_product_details(self) -> dict:
        """
        Get product details from a given product URL.
        """
        try:
            # Retrieve tags from specifications
            tag_product_spec_titles = self._soup.find_all(
                "td", class_="b-pdp_specification-label"
            )
            tag_product_specs = self._soup.find_all(
                "td", class_="b-pdp_specification-value"
            )

            # Retrieve text from tags and normalize it
            product_spec_titles = [
                normalize_string(el.text) for el in tag_product_spec_titles
            ]
            product_spec = [el.text for el in tag_product_specs]

            # Create a dictionary with product specifications
            product_specs = dict(zip(product_spec_titles, product_spec))

            return product_specs
        except Exception as e:
            print(f'error while retrieving product details: {e}')
    def get_all_data(self) -> dict:
        """
        Get all data from the product detail page.
        """
        final_data = {}

        try:
            final_data["specs"] = self.get_product_details()
            final_data["price"] = self.get_price()
            final_data["url"] = self.detail_url
        except Exception as e:
            print(f"Error occurred while scraping product details: {e}")
            final_data = {}

        return final_data
