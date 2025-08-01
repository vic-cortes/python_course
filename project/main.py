from src.scraper import (
    HomeDepotDetailScraper,
    HomeDepotParentScraper,
    LiverpoolDetailScraper,
    LiverpoolParentScraper,
)
from src.scraper.utils import get_firefox_driver

if __name__ == "__main__":
    driver = get_firefox_driver()
    scraper = LiverpoolParentScraper(driver=driver)

    product_links = scraper.get_product_links()

    all_data = []

    for link in product_links:
        detail_scraper = LiverpoolDetailScraper(driver=driver, detail_url=link)

        try:
            product_details = detail_scraper.get_all_data()
        except Exception as e:
            print(f"Error occurred while scraping {link}: {e}")
            continue

        all_data.append(product_details)

    print(all_data)
    driver.quit()
