from core.configs import settings
from sqlalchemy import Column, Integer, String


class ShoesModel(settings.DBBaseModel): #DBBaseModel é a base declarativa
    
    __tablename__ = "Shoes"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    brand: str = Column(String(200),unique=True)
    gender: str = Column(String(200))
    numbering: int = Column(String(200))
    color: str = Column(String(200))
    