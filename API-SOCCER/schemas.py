from pydantic import BaseModel
from typing import Optional

class TeamSoccerBase(BaseModel):
    name: str
    numberFans: int
    city : str
    founded : int
    stadium_name : str
    number_titles : int
    coach : str
    league : str
    
class TeamSoccerCreate(TeamSoccerBase):
    pass

class TeamSoccerResponse(TeamSoccerBase):
    id: int
    
#class TeamSoccerDelete(BaseModel):
#   id : int

    

class TeamSoccerUpdate(BaseModel):
    name: Optional[str] = None
    numberFans: Optional[int] = None
    city : Optional[str] = None
    founded : Optional[int] = None
    stadium_name : Optional[str] = None
    number_titles : Optional[int] = None
    coach : Optional[str] = None
    league : Optional[str] = None
    
    class Config:
        from_attributes = True 
    
    