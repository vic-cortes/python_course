from sqlalchemy import Column, Float, Integer, String

from ..db.base_class import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    rfc = Column(String(255), unique=True, nullable=True)

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name})>"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
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

    def __repr__(self):
        return f"<Product(id={self.id}, brand={self.brand}, price={self.price})>"
