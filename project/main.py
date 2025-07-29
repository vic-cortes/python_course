from src.scraper import (
    HomeDepotDetailScraper,
    HomeDepotParentScraper,
    LiverpoolDetailScraper,
    LiverpoolParentScraper,
)
from src.scraper.utils import get_firefox_driver

if __name__ == "__main__":
    driver = get_firefox_driver()
    scraper = HomeDepotParentScraper(driver=driver)

    product_links = scraper.get_product_links()

    all_data = []

    for link in product_links:
        detail_scraper = HomeDepotDetailScraper(driver=driver, detail_url=link)
        product_details = detail_scraper.get_all_data()
        all_data.append(product_details)

    print(all_data)
    driver.quit()
