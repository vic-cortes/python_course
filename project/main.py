import asyncio
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from src.scraper import (
    HomeDepotDetailScraper,
    HomeDepotParentScraper,
    LiverpoolDetailScraper,
    LiverpoolParentScraper,
)
from src.scraper.base import BaseScraper
from src.scraper.constants import DATA_PATH
from src.scraper.utils import get_firefox_driver

SUPPORTED_SCRAPERS = {
    "liverpool": {
        "parent": LiverpoolParentScraper,
        "detail": LiverpoolDetailScraper,
    },
    "home_depot": {
        "parent": HomeDepotParentScraper,
        "detail": HomeDepotDetailScraper,
    },
}


# Función sincrónica
def tarea_sincrona(valor):
    time.sleep(1)
    return f"Resultado {valor}"


def store_data(scraper: BaseScraper, all_data):
    current_time = datetime.now().strftime("%Y%m%d_%H_00")
    current_client_path = DATA_PATH / scraper.service_name

    # Check if folder exists, if not create it
    if not current_client_path.exists():
        current_client_path.mkdir(parents=True)

    output_file = current_client_path / f"products_{current_time}.json"

    with open(output_file, "w") as file:
        json.dump(all_data, file, indent=4)


# Función async que ejecuta concurrentemente
async def arun_scraper(scraper_name: str) -> None:
    if scraper_name not in SUPPORTED_SCRAPERS:
        raise ValueError(f"Unsupported scraper: {scraper_name}")

    ParentScraper = SUPPORTED_SCRAPERS[scraper_name]["parent"]
    DetailScraper = SUPPORTED_SCRAPERS[scraper_name]["detail"]

    driver = get_firefox_driver(headless=True)
    scraper: BaseScraper = ParentScraper(driver=driver)
    product_links = scraper.get_all_links()
    # driver.quit()

    all_data = []

    # async def execute_and_store_data(url: str):
    #     # driver = get_firefox_driver(headless=True)
    #     detail_scraper: BaseScraper = DetailScraper(driver=driver, detail_url=url)
    #     resultado = await asyncio.to_thread(detail_scraper.get_all_data)
    #     all_data.append(resultado)

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=20) as pool:

        async def execute_and_store_data(driver, url):
            detail_scraper: BaseScraper = DetailScraper(driver=driver, detail_url=url)
            resultado = await loop.run_in_executor(pool, detail_scraper.get_all_data)
            all_data.append(resultado)

        tareas = [execute_and_store_data(driver, url) for url in product_links]
        await asyncio.gather(*tareas)

    # tareas = [execute_and_store_data(url) for url in product_links]
    # await asyncio.gather(*tareas)
    print("Resultados:", all_data)
    driver.quit()

    store_data(scraper, all_data)


# asyncio.run(arun_scraper("home_depot"))


def run_scraper(scraper_name: str) -> None:
    """
    Run the specified scraper and save the results to a JSON file.
    """
    if scraper_name not in SUPPORTED_SCRAPERS:
        raise ValueError(f"Unsupported scraper: {scraper_name}")

    ParentScraper = SUPPORTED_SCRAPERS[scraper_name]["parent"]
    DetailScraper = SUPPORTED_SCRAPERS[scraper_name]["detail"]

    driver = get_firefox_driver(headless=True)
    scraper: BaseScraper = ParentScraper(driver=driver)

    product_links = scraper.get_all_links()

    all_data = []

    for link in product_links:
        detail_scraper = DetailScraper(driver=driver, detail_url=link)

        try:
            product_details = detail_scraper.get_all_data()
        except Exception as e:
            print(f"Error occurred while scraping {link}: {e}")
            continue

        all_data.append(product_details)

    store_data(scraper, all_data)

    driver.quit()


if __name__ == "__main__":
    scraper_name = "home_depot"
    # run_scraper(scraper_name)
    asyncio.run(arun_scraper(scraper_name))
