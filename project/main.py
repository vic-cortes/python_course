from src.scraper.liverpool import LiverpoolScraper
from src.scraper.utils import get_firefox_driver

if __name__ == "__main__":
    driver = get_firefox_driver()
    scraper = LiverpoolScraper(driver=driver)

    try:
        product_links = scraper.get_product_links()
        print("Product Links:", product_links)
    finally:
        driver.quit()
