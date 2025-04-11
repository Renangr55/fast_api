import uvicorn
from typing import Union
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from fastapi import FastAPI, HTTPException, status, Response, Depends
from sqlalchemy import select
from database import engine, Base, get_db
from models import SoccerTeam
from schemas import TeamSoccerBase, TeamSoccerCreate, TeamSoccerResponse
from sqlalchemy.future import select

app = FastAPI(title='SoccerAPI', description='created Soccer API')

@app.get('/')
async def get_test():
    return {'sucess': 'foii'}

@app.get('/SocccerTeams/')
async def get_soccer_teams(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(SoccerTeam))
    team_soccers = results.scalars().all() # usando scalars para extrair as informações de uma unica coluna
    return {"team_soccers": team_soccers}
    


@app.post('/SocccerTeams/Criar/',status_code=status.HTTP_201_CREATED)
async def create_soccer_teams(SoccerTeams: TeamSoccerBase, db: AsyncSession = Depends(get_db)):
   
    db_soccerTeam = SoccerTeam(**SoccerTeams.model_dump())
    db.add(db_soccerTeam)
    await db.commit()
    await db.refresh(db_soccerTeam)
    return db_soccerTeam

@app.delete('/SoccerTeams/deletar/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_soccer_teams(soccerTeams: TeamSoccerBase, db: AsyncSession = Depends(get_db)):
    query = select(SoccerTeam).where(SoccerTeam.name == soccerTeams.name)
    result = await db.execute(query)
    db_team_name = result.scalar_one_or_none()
    
    if db_team_name is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")

    await db.delete(db_team_name)
    await db.commit()
    return None


@app.get("/SocccerTeams/id")
async def get_team(SoccerTeams: TeamSoccerBase,db: AsyncSession = Depends(get_db)):
    result = select(SoccerTeam).where(SoccerTeam.name == SoccerTeams.name)
    db_team_name = result.scalar_one_or_none()
    
    if db_team_name is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")

    await db.delete(db_team_name)
    await db.commit()
    return None

        


    
    

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
  




