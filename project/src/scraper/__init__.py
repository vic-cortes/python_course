# Make scraper a proper package
from .home_depot import DetailScraper as HomeDepotDetailScraper
from .home_depot import ParentScraper as HomeDepotParentScraper
from .liverpool import DetailScraper as LiverpoolDetailScraper
from .liverpool import ParentScraper as LiverpoolParentScraper
from .utils import get_firefox_driver

__all__ = [
    "LiverpoolParentScraper",
    "LiverpoolDetailScraper",
    "HomeDepotParentScraper",
    "HomeDepotDetailScraper",
    "get_firefox_driver",
]


SUPPORTED_SCRAPERS = ["liverpool", "home_depot"]
