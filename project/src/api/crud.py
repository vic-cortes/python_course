from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from ..models.products import Product


def get_client_product(db: Session, client_name: str) -> list[Product]:
    """
    Retrieve a single AI app based on its client_name.
    """
    return db.query(Product).filter(Product.client_name == client_name).all()
