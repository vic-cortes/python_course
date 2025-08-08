from db.base_class import Base
from sqlalchemy import Column, Integer, String


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name})>"
