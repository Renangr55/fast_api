from typing import Optional
from pydantic import BaseModel as SCBaseModel # mudando para não confundir com o basemodel do sqlachemy

class ShoesSchemas(SCBaseModel):
    id: Optional[int] = None
    brand: str
    gender: str
    numbering: int
    color: str
    
    class Config:
        orm_mode = True # aqui o pydanbtic aceita receber objetos,ai ele pode receber modelos alchemt, por que le só vai ler os atribustos