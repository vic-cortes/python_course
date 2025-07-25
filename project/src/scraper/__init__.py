# Make scraper a proper package
from .liverpool import LiverpoolDetailScraper, LiverpoolScraper
from .utils import get_firefox_driver

__all__ = [
    "LiverpoolScraper",
    "LiverpoolDetailScraper",
    "get_firefox_driver",
]
