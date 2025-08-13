from dataclasses import dataclass

from src.scraper import SUPPORTED_SCRAPERS

print("Supported scrapers:", SUPPORTED_SCRAPERS)


@dataclass
class EtlSchema:
    brand: str
    color: str
    price: float
    url: str
    rpm: str
    product_type: str
    model: str
    ancho: str
    alto: str
    capacidad: str
    client_name: str
