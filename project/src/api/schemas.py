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


class MetadataSchema(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    page_size: int
    has_next: bool
    has_previous: bool


class ResponseSchema(BaseModel):
    items: list[ScraperSchema]
    metadata: MetadataSchema
