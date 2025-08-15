# Import models here
from ..models.clients import Client
from ..models.products import Product
from .base_class import Base

if __name__ == "__main__":
    # Adding to prevent ruff remove this import
    Client()
    Product()
    Base()
