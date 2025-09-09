import asyncio
import json
from enum import Enum

from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    JsonCssExtractionStrategy,
)


class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"


browser_config = BrowserConfig(browser_type=BrowserType.FIREFOX.value, headless=False)
BASE_URL = "https://ddtech.mx"
PRODUCT_URL = f"{BASE_URL}/productos?categoria=notebooks"


async def main():
    # ✅ Inspeccionando DDTech, los productos están en <div class="productCard">
    KEY_CSS_SELECTOR = "div.productCard"

    output_schema = {
        "name": "DDTech Laptop Scraper",
        "baseSelector": "div.productCard",
        "fields": [
            {"name": "title", "selector": "h2.cardTitle a", "type": "text"},
            {"name": "price", "selector": "span.price", "type": "text"},
            {
                "name": "details_url",
                "selector": "h2.cardTitle a",
                "type": "attribute",
                "attribute": "href",
            },
            {
                "name": "availability",
                "selector": "span.stock",
                "type": "text",
            },
        ],
    }

    strategy = JsonCssExtractionStrategy(output_schema)
    crawler_config = CrawlerRunConfig(
        extraction_strategy=strategy,
        wait_for=KEY_CSS_SELECTOR,
        wait_for_timeout=15,  # tiempo de espera más largo porque DDTech a veces es lento
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=PRODUCT_URL, config=crawler_config)

        if result.success:
            dict_data = json.loads(result.extracted_content)

            # ✅ Aseguramos URLs absolutas
            for element in dict_data:
                if not element["details_url"].startswith("http"):
                    element["details_url"] = f"{BASE_URL}{element['details_url']}"

            with open("ddtech_laptops.json", "w", encoding="utf-8") as file:
                json.dump(dict_data, file, indent=4, ensure_ascii=False)

            print(f"✅ {len(dict_data)} productos guardados en ddtech_laptops.json")

        else:
            print("❌ No se pudo scrapear DDTech")


if __name__ == "__main__":
    asyncio.run(main())
