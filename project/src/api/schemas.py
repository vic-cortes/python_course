from pydantic import BaseModel


class ScraperSchema(BaseModel):
    brand: str
    color: str
    price: float
    url: str | None = None
    rpm: str
    product_type: str
    model: str
    ancho: str
    alto: str
    capacidad: str
    client_name: str
