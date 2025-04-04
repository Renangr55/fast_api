from typing import Optional

from pydantic import BaseModel

class Pato(BaseModel):
    id: Optional[int] = None
    nome: str
    especie: str
    idade: str
    cor: str
    foto: str