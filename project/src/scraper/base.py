from abc import ABC

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseScraper(ABC):
    """
    Base class for web scrapers.
    """

    @property
    def service_name(self) -> str:
        return "base"

    def _ensure_key_product_tags_exists(
        self,
        value: str,
        by_type: By = By.CLASS_NAME,
        timeout: int = 5,
    ) -> None:
        """
        Wait until a product tag is present on the page.
        """
        # wait until a tag with class exists
        try:
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located((by_type, value))
            )
        except (TimeoutException, NoSuchElementException):
            raise ValueError("Product tag not found or not loaded properly.")
