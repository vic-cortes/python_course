import json
from dataclasses import dataclass

from src.scraper import SUPPORTED_SCRAPERS
from src.scraper.constants import DATA_PATH

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


DEFAULT_NOT_AVAILABLE = "N/A"


@dataclass
class LiverpoolEtlSchema:
    client_name: str = "liverpool"
    specs: dict = None
    price: float = 0.0
    url: str = ""
    product_type: str = "lavadora"

    @property
    def brand(self):
        return self.specs.get("marca", DEFAULT_NOT_AVAILABLE).upper().strip()

    @property
    def color(self):
        return self.specs.get("color", DEFAULT_NOT_AVAILABLE).upper().strip()

    @property
    def rpm(self):
        return self.specs.get("velocidad_maxima", DEFAULT_NOT_AVAILABLE).upper().strip()

    @property
    def model(self):
        return self.specs.get("modelo_comercial", DEFAULT_NOT_AVAILABLE).upper().strip()

    @property
    def ancho(self):
        return (
            self.specs.get("ancho_del_producto", DEFAULT_NOT_AVAILABLE).upper().strip()
        )

    @property
    def alto(self):
        return (
            self.specs.get("alto_del_producto", DEFAULT_NOT_AVAILABLE).upper().strip()
        )

    @property
    def capacidad(self):
        return (
            self.specs.get("capacidad_compatible", DEFAULT_NOT_AVAILABLE)
            .upper()
            .strip()
        )

    def to_dict(self):

        if self.specs is None:
            return {}

        return {
            "client_name": self.client_name,
            "brand": self.brand,
            "color": self.color,
            "price": self.price,
            "url": self.url,
            "rpm": self.rpm,
            "product_type": self.product_type,
            "model": self.model,
            "ancho": self.ancho,
            "alto": self.alto,
            "capacidad": self.capacidad,
        }


available_paths = [DATA_PATH / scraper for scraper in SUPPORTED_SCRAPERS]

print("Available data paths:", available_paths)

data_path = DATA_PATH / "liverpool"
data_files = list(data_path.glob("*.json"))

data_contents = []

for file in data_files:
    with open(file, "r") as f:
        json_data = json.load(f)

        for element in json_data:
            schema = LiverpoolEtlSchema(**element)

            if new_data := schema.to_dict():
                data_contents.append(schema.to_dict())

print(f"Data contents from {data_contents[0]}")


# Read all files in the data directory
