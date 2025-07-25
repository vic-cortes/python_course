# Make scraper a proper package
from .liverpool import DetailScraper, ParentScraper
from .utils import get_firefox_driver

__all__ = [
    "ParentScraper",
    "DetailScraper",
    "get_firefox_driver",
]
