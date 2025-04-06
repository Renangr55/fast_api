import uvicorn
from typing import Union
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from fastapi import FastAPI, HTTPException, status, Response, Depends
from sqlalchemy import select
from database import engine, Base, get_db
from models import SoccerTeam
from schemas import TeamSoccerBase, TeamSoccerCreate, TeamSoccerResponse


app = FastAPI(title='SoccerAPI', description='created Soccer API')

@app.get('/')
async def get_test():
    return {'sucess': 'foii'}

@app.get('/teste/SocccerTeams/')
async def get_soccer_teams(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(SoccerTeam))
    team_soccers = results.scalars().all()
    return {"team_soccers": team_soccers}
    



@app.post('/teste/SocccerTeams/',status_code=status.HTTP_201_CREATED)
async def create_soccer_teams(SoccerTeams: TeamSoccerBase, db: AsyncSession = Depends(get_db)):
   
    db_soccerTeam = SoccerTeam(**SoccerTeams.model_dump())
    db.add(db_soccerTeam)
    await db.commit()
    await db.refresh(db_soccerTeam)
    return db_soccerTeam
    
        


    
    

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
  




