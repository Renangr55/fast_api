from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import  Mapped, MappedColumn
from database import Base
from pydantic import BaseModel, create_model
from typing import Optional

class SoccerTeam (Base):
    
    __tablename__ = "soccer_teams"
    
    id: Mapped[int] = MappedColumn(Integer,primary_key=True) 
    name: Mapped[str] = MappedColumn(String,unique=True, nullable=False)
    numberFans: Mapped[int] = MappedColumn(unique=True, nullable=False)
    
    
    
    
    