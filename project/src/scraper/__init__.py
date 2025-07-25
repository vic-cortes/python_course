# Make scraper a proper package
from .liverpool import LiverpoolScraper
from .utils import get_firefox_driver

__all__ = ["LiverpoolScraper", "get_firefox_driver"]
