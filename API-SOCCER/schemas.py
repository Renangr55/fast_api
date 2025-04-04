from pydantic import BaseModel
from typing import Optional

class TeamSoccerBase(BaseModel):
    name: str
    numberFans: int
    
class TeamSoccerCreate(TeamSoccerBase):
    pass

class TeamSoccerResponse(TeamSoccerBase):
    id: int
    
    class Config:
        from_attributes = True 
    
    