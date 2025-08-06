import json
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


def run_scraper(scraper_name: str) -> None:
    """
    Run the specified scraper and save the results to a JSON file.
    """
    if scraper_name not in SUPPORTED_SCRAPERS:
        raise ValueError(f"Unsupported scraper: {scraper_name}")

    ParentScraper = SUPPORTED_SCRAPERS[scraper_name]["parent"]
    DetailScraper = SUPPORTED_SCRAPERS[scraper_name]["detail"]

    driver = get_firefox_driver()
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

    current_time = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = DATA_PATH / f"{scraper.service_name}_products_{current_time}.json"

    with open(output_file, "w") as file:
        json.dump(all_data, file, indent=4)

    driver.quit()


if __name__ == "__main__":
    scraper_name = "home_depot"
    run_scraper(scraper_name)
