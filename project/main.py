from src.scraper.liverpool import LiverpoolDetailScraper, LiverpoolScraper
from src.scraper.utils import get_firefox_driver

if __name__ == "__main__":
    driver = get_firefox_driver()
    scraper = LiverpoolScraper(driver=driver)

    product_links = scraper.get_product_links()

    all_data = []

    for link in product_links:
        detail_scraper = LiverpoolDetailScraper(driver=driver, detail_url=link)
        product_details = detail_scraper.get_product_details()
        all_data.append(product_details)

    print(all_data)
    driver.quit()
