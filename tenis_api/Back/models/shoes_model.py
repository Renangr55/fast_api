from core.configs import settings
from sqlalchemy import Column, Integer, String, Numeric
from decimal import Decimal


class ShoesModel(settings.DBBaseModel): #DBBaseModel é a base declarativa
    
    __tablename__ = "Shoes"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    brand: str = Column(String(200))
    price:  Numeric = Column(Numeric(10,2))
    gender: str = Column(String(200))
    numbering: Integer = Column(Integer)
    color: str = Column(String(200))
    description: str = Column(String(500))
    
    
    