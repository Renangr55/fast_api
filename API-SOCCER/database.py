from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#driver: aiosqlite

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", connect_args={"check_same_thread": False}) # Criando um motor do banco de dados assincrono
SessionLocal = async_sessionmaker(engine)  
Base = declarative_base() #convertendo as classes para para modelos SQL Alchemy

async def get_db():
    #iniciando a transição assincrona
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.create_all) # criando todos os modelos no banco de dados
    db = SessionLocal()
    try: 
        yield db #executar o banco
    finally:
        await db.close()