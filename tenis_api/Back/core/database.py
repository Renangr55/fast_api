from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings
from sqlalchemy.orm import sessionmaker



engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, echo=True)


Session: AsyncEngine = sessionmaker( #sessionmaker é usado para criar uma session com varios argumentos
    autoflush=False,
    expire_on_commit=False,
    class_= AsyncSession, # subclasse de  personalizada de sessionmaker
    bind=engine,
    

    
)
