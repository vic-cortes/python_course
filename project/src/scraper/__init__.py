# Make scraper a proper package
from .home_depot import DetailScraper as HomeDepotDetailScraper
from .home_depot import ParentScraper as HomeDepotParentScraper
from .liverpool import DetailScraper as LiverpoolDetailScraper
from .liverpool import ParentScraper as LiverpoolParentScraper
from .palacio import DetailScraper as PalacioDetailScraper
from .palacio import ParentScraper as PalacioParentScraper
from .utils import get_firefox_driver

__all__ = [
    "LiverpoolParentScraper",
    "LiverpoolDetailScraper",
    "HomeDepotParentScraper",
    "HomeDepotDetailScraper",
    "PalacioParentScraper",
    "PalacioDetailScraper",
    "get_firefox_driver",
]


SUPPORTED_SCRAPERS = ["liverpool", "home_depot", "palacio"]
