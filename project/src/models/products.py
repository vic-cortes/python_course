from sqlalchemy import Column, DateTime, Float, Integer, String

from ..db.base_class import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(255), nullable=False)
    brand = Column(String(255))
    color = Column(String(255))
    price = Column(Float)
    url = Column(String(255))
    rpm = Column(String(255))
    product_type = Column(String(255))
    model = Column(String(255))
    ancho = Column(String(255))
    alto = Column(String(255))
    capacidad = Column(String(255))
    date_created = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Product(id={self.id}, brand={self.brand}, price={self.price})>"
