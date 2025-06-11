from typing import Optional
from pydantic import BaseModel as SCBaseModel, condecimal # mudando para não confundir com o basemodel do sqlachemy

class ShoesSchemas(SCBaseModel):
    id: Optional[int] = None
    name: str
    brand: str
    price: condecimal(max_digits=10, decimal_places=2) 
    gender: str
    numbering: int
    color: str
    description: str
    
    class Config:
        from_attributes = True # aqui o pydanbtic aceita receber objetos,ai ele pode receber modelos alchemt, por que le só vai ler os atribustos