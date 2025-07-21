import requests
from bs4 import BeautifulSoup

HOME_DEPOT_URL = "https://www.homedepot.com.mx/b/linea-blanca-y-cocinas/lavadoras-y-secadoras/lavadoras"
SORIANA_URL = (
    "https://www.soriana.com/hogar-y-electrodomesticos/linea-blanca/lavadoras/"
)
PALACIO_DE_HIERRO_URL = "https://www.elpalaciodehierro.com/buscar?q=lavadoras"


# https://www.homedepot.com.mx/p/maytag-lavadora-maytag-22-kg-load-go-he-7mmhw6621hw-151135


response = requests.get(HOME_DEPOT_URL)
soup = BeautifulSoup(response.content, "html.parser")

response_soriana = requests.get(SORIANA_URL)
soup_soriana = BeautifulSoup(response_soriana.content, "html.parser")

response_palacio = requests.get(PALACIO_DE_HIERRO_URL)
soup_palacio = BeautifulSoup(response_palacio.content, "html.parser")

headers = {
    "WCTrustedToken": "365818367%2CA%2Fy2rRq2lfBwvwQHgeBHS3cqROS4tQzG8%2FfO9fNJMAE%3D",
    "sec-ch-ua-platform": '"macOS"',
    "Referer": "https://www.homedepot.com.mx/b/linea-blanca-y-cocinas/lavadoras-y-secadoras/lavadoras",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "WCToken": "365818367%2CejjOoDZhy3c9If0hOxSHVDMQBE6kiRrOTGfrxyrUA6oksn1SJ6Kv7CdJy6JB7c34L61xKKZeYuVxA8f0tHGZ9fXtES8lDszK00AU049lcO0Zc45%2BgrhN%2Br03M2P1BctYHBeB6PKXM5WXXQ7mvHHLgpkth2OKYAgwIZJ3HEuuTEZPHyc4lSfnF%2BYHaBAuaIW0JXoHRpHk2LWfok1q8FrO%2F7LGWLiyTsbrZHK%2FxGQdq%2FSsI%2BFtD0wNUXl73hTeJnoIWsDhqU2kB47losDzPAmr4Q%3D%3D",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
}

params = {
    "storeId": "10351",
    "categoryId": "24008",
    "limit": "28",
    "offset": "0",
    "contractId": "4000000000000000003",
    "currency": "MXN",
    "langId": "-5",
    "marketId": "21",
    "stLocId": "12605",
    "extendedCatalog": "false",
    "marketOnly": "true",
    "physicalStoreId": "8702",
    "profileName": "HCL_V2_findProductsByCategoryWithPriceRangeSequenceTest",
    "selectedFacets": "[object Object]",
    "minPrice": "-1",
    "maxPrice": "-1",
    "selectedPageOffset": "0",
    "orderBy": "0",
}

response = requests.get(
    "https://www.homedepot.com.mx/search/resources/api/v2/products",
    params=params,
    headers=headers,
)

print(response)

import os

from constants import GECKO_DRIVER_PATH
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOAD_TIMEOUT = 10
STRATEGY = "none"

options = Options()
options.headless = False  # No mostrar explorador

options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/110.0",
)


capabilities = DesiredCapabilities.FIREFOX
capabilities["pageLoadStrategy"] = STRATEGY


service = Service(executable_path=GECKO_DRIVER_PATH, log_path=os.path.devnull)
driver = webdriver.Firefox(options=options, service=service)
driver.set_page_load_timeout(LOAD_TIMEOUT)

driver.get(HOME_DEPOT_URL)

# Esperar a que un elemento importante esté presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div#productCard_a_1_2044157"))
)
html = BeautifulSoup(driver.page_source, "html.parser")
products_container = html.find("div", class_="product-listing-container")

driver.quit()
