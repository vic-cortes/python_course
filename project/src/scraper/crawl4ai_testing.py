import asyncio
import json

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    JsonCssExtractionStrategy,
)
from crawl4ai.models import CrawlResultContainer

browser_config = BrowserConfig(browser_type="firefox", headless=False)
BASE_URL = "https://www.liverpool.com.mx"
PRODUCT_URL = f"{BASE_URL}/tienda?s=lavadoras"


async def main():
    schema = {
        "name": "Liverpool Product Scraper",
        "baseSelector": "li.m-product__card",
        "fields": [
            {"name": "title", "selector": "h3.card-title", "type": "text"},
            {"name": "brand", "selector": "h3.a-card-brand", "type": "text"},
            {"name": "price", "selector": "p.a-card-price", "type": "text"},
            {
                "name": "details_url",
                "selector": "a",
                "type": "attribute",
                "attribute": "href",
            },
        ],
    }

    strategy = JsonCssExtractionStrategy(schema)

    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Run the crawler on a URL
        result: CrawlResultContainer = await crawler.arun(
            url=PRODUCT_URL,
            config=CrawlerRunConfig(extraction_strategy=strategy),
        )

        # Print the extracted content
        print(result.markdown)

        if result.success:
            # Save the result to a JSON file
            with open("liverpool_products.json", "w") as file:
                dict_data = json.loads(result.extracted_content)
                json.dump(dict_data, file, indent=4)
            print("Data saved to liverpool_products.json")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
