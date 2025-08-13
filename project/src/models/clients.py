from sqlalchemy import Column, Float, Integer, String

from ..db.base_class import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    rfc = Column(String(255), unique=True, nullable=True)

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name})>"
