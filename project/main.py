from src.scraper.liverpool import LiverpoolDetailScraper, LiverpoolScraper
from src.scraper.utils import get_firefox_driver

if __name__ == "__main__":
    driver = get_firefox_driver()
    scraper = LiverpoolScraper(driver=driver)

    product_links = scraper.get_product_links()

    for link in product_links:
        LiverpoolDetailScraper(driver=driver, product_url=link)
