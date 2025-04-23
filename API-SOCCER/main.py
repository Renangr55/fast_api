import uvicorn
from typing import Union
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from fastapi import FastAPI, HTTPException, status, Response, Depends , Query, Path
from sqlalchemy import select
from database import engine, Base, get_db, init_db
from models import SoccerTeam
from schemas import TeamSoccerBase, TeamSoccerCreate, TeamSoccerResponse, TeamSoccerUpdate
from sqlalchemy.future import select



app = FastAPI(title='SoccerAPI', description='created Soccer API')



@app.get('/')
async def get_test():
    return {'sucess': 'foii'}

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get('/SocccerTeams/')
async def get_soccer_teams(db: AsyncSession = Depends(get_db)): 
    results = await db.execute(select(SoccerTeam))
    team_soccers = results.scalars().all() # usando scalars para extrair as informações de uma unica coluna
    return {"team_soccers": team_soccers}
    

@app.post('/SocccerTeams/Create/',status_code=status.HTTP_201_CREATED)
async def create_soccer_teams(SoccerTeams: TeamSoccerBase, db: AsyncSession = Depends(get_db)):
   
    db_soccerTeam = SoccerTeam(**SoccerTeams.model_dump())
    db.add(db_soccerTeam)
    await db.commit()
    await db.refresh(db_soccerTeam)
    return db_soccerTeam

@app.delete('/SoccerTeams/delete/{team_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_soccer_teams(team_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(SoccerTeam).where(SoccerTeam.id == team_id))
    db_team_name = result.scalar_one_or_none()
    
    if db_team_name is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")

    await db.delete(db_team_name)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get("/SocccerTeams/name")
async def get_team_by_name(name: str = Query(description="Team name"), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SoccerTeam).where(SoccerTeam.name == name))
    db_team = result.scalar_one_or_none()
    
    if db_team is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")


    return db_team

@app.patch('/SocccerTeams/atualizar/{team_id}', response_model=TeamSoccerResponse)
async def Update_soccer_team(  team_id: int = Path(description="ID do time a ser atualizado"), update_data: TeamSoccerUpdate = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(SoccerTeam).where(SoccerTeam.id == team_id))
    db_team = result.scalar_one_or_none()

    if db_team is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")

    update_dict = update_data.dict(exclude_unset=True)

    for field, value in update_dict.items():
        setattr(db_team, field, value) #update of fields 

    await db.commit()
    await db.refresh(db_team)

    return db_team
    
    
        


    
    

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
  




