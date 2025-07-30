from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base import BaseScraper
from .utils import normalize_string

BASE_URL = "https://www.homedepot.com.mx"
PRODUCT_URL = f"{BASE_URL}/s/lavadoras"


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
        self._ensure_key_product_tags_exists("MuiCardContent-root", timeout=10)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        product_items = soup.select("div.MuiCardContent-root")

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
    KEY_PRODUCT_TAG = "pdp-spec-tecnicas"

    def __post_init__(self):
        self.driver.get(self.detail_url)
        self._ensure_key_product_tags_exists(self.KEY_PRODUCT_TAG, by_type=By.ID, timeout=10)
        self._soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def get_price(self) -> str:
        """
        Get the price of the product from the detail page.
        """
        JUST_ONE_PRICE = 1

        price_node = self._soup.find("div", class_="price-card-height")
        # Get price node then find all paragraphs with class `product-price`
        # Confirm if `\xa0` is always present
        prices = [el.text.strip() for el in price_node.find_all("p") if "product-price" in el["class"]]

        if len(prices) != JUST_ONE_PRICE:
            raise ValueError("Price not found on the page.")

        # Divide by 100 due special character `\xa0`
        raw_price = prices[0]
        string_price = [el for el in list(raw_price) if el.isdigit()]
        return float("".join(string_price)) / 100

    def get_product_details(self) -> dict:
        """
        Get product details from a given product URL.
        """
        # Find by id instead of class
        product_details = self._soup.find("div", id="pdp-spec-tecnicas")

        if not product_details:
            return {}
        # Find all titles, all titles have style `font-weight: 600;`
        _, *tag_product_specs = product_details.find_all("p")
        # First element is the title, the rest are specifications

        product_spec_titles = [
            normalize_string(el.text) for el in tag_product_specs if el.get("style")
        ]
        product_spec = [
            el.text for el in tag_product_specs if not el.get("style")
        ]

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
