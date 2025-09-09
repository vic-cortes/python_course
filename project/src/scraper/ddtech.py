from __future__ import annotations
import time
import re
from dataclasses import dataclass
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import BaseScraper
from .utils import get_firefox_driver

BASE_URL = "https://ddtech.mx"
PRODUCT_URL = f"{BASE_URL}/productos/computadoras/portatiles"


@dataclass
class DDTechParentScraper(BaseScraper):
    driver: webdriver.Firefox

    @property
    def service_name(self) -> str:
        return "ddtech"

    def go_to_main_page(self) -> None:
        print(f"* Navegando a {PRODUCT_URL}")
        self.driver.get(PRODUCT_URL)
        time.sleep(5)  # Esperar a que carguen productos

    def get_product_links(self, max_products: int = 20) -> list[str]:
        """
        Extrae los enlaces de productos en la página principal.
        """
        self.go_to_main_page()
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        product_links = []

        # Selector que funciona en DDTech para laptops
        links = soup.select('div.product-image a[href^="https://ddtech.mx/producto/"]')

        for a in links:
            href = a.get('href')
            if href and href.startswith('https://ddtech.mx/producto/') and 'id=' in href:
                if href not in product_links:
                    product_links.append(href)
            if len(product_links) >= max_products:
                break

        print(f"🔗 Encontrados {len(product_links)} productos en esta página")
        return product_links

    def scroll_and_collect(self, max_products: int = 20) -> list[str]:
        """
        Scroll infinito para cargar productos dinámicamente.
        """
        self.go_to_main_page()
        SCROLL_PAUSE_TIME = 3
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        all_links = set()

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            links = self.get_product_links(max_products)
            all_links.update(links)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height or len(all_links) >= max_products:
                break
            last_height = new_height

        print(f"✅ Total de productos recolectados: {len(all_links)}")
        return list(all_links)


@dataclass
class DDTechDetailScraper(BaseScraper):
    driver: webdriver.Firefox
    detail_url: str

    def __post_init__(self):
        print(f"* Scrapeando detalle: {self.detail_url}")
        self.driver.get(self.detail_url)
        time.sleep(3)
        self._soup = BeautifulSoup(self.driver.page_source, "html.parser")

    def get_name(self) -> str:
        name_node = self._soup.select_one('title')
        return name_node.get_text(strip=True) if name_node else "No encontrado"

    def get_price(self) -> str:
        price_node = self._soup.select_one('span[class*="price"]')
        if price_node:
            price_text = price_node.get_text(strip=True)
            price_clean = re.sub(r'[^\d.,]', '', price_text)
            return price_clean if price_clean else price_text
        return "No encontrado"

    def get_sku(self) -> str:
        match = re.search(r'id=(\d+)', self.detail_url)
        return match.group(1) if match else "No encontrado"

    def get_description(self) -> str:
        desc_node = self._soup.select_one('[class*="description-container"]')
        return desc_node.get_text(strip=True)[:500] if desc_node else "No encontrado"

    def get_availability(self) -> str:
        avail_node = self._soup.select_one('[class="col-sm-9"]')
        return avail_node.get_text(strip=True) if avail_node else "No encontrado"

    def get_all_data(self) -> dict:
        return {
            "url": self.detail_url,
            "nombre": self.get_name(),
            "precio": self.get_price(),
            "sku": self.get_sku(),
            "descripcion": self.get_description(),
            "disponibilidad": self.get_availability()
        }
