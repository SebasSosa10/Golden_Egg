from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    on_offer = Column(Boolean, default=True)