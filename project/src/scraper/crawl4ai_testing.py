import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig

browser_config = BrowserConfig(browser_type="firefox", headless=False)


async def main():

    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(url="https://crawl4ai.com")

        # Print the extracted content
        print(result.markdown)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
