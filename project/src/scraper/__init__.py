# src/scraper/__init__.py

from .home_depot import DetailScraper as HomeDepotDetailScraper
from .home_depot import ParentScraper as HomeDepotParentScraper
from .liverpool import DetailScraper as LiverpoolDetailScraper
from .liverpool import ParentScraper as LiverpoolParentScraper
from .ddtech import DDTechDetailScraper
from .ddtech import DDTechParentScraper
from .utils import get_firefox_driver

__all__ = [
    "DDTechParentScraper",
    "DDTechDetailScraper",
    "LiverpoolParentScraper",
    "LiverpoolDetailScraper",
    "HomeDepotParentScraper",
    "HomeDepotDetailScraper",
    "get_firefox_driver",
]

# Normalizamos nombres de scrapers soportados
SUPPORTED_SCRAPERS = ["ddtech", "liverpool", "home_depot"]
