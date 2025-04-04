from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", connect_args={"check_same_thread": False}) # Criando um motor do banco de dados assincrono
SessionLocal = async_sessionmaker(engine)
Base = declarative_base()

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = SessionLocal()
    try: 
        yield db
    finally:
        await db.close()