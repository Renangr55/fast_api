from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#driver: aiosqlite

DATABASE_URL = "sqlite+aiosqlite:///db.sqlite3"

engine = create_async_engine( # Criando um motor do banco de dados assincrono
    DATABASE_URL,
    connect_args={"check_same_thread": False}, #permitindo que eles possa usar várias thread
    pool_pre_ping=True, #testando a conexão
    echo=True 
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)  
Base = declarative_base() #convertendo as classes para para modelos SQL Alchemy

async def get_db():
    db = SessionLocal()
    try: 
        yield db #executar o banco
    finally:
        await db.close()
        
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # criando todos os modelos no banco de dados