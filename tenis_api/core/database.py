from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_session
from core.configs import settings


engine: AsyncEngine = create_async_engine(settings.DATABASE_URL)
Session: AsyncEngine = sessionmaker( #sessionmaker é usado para criar uma session com varios argumentos
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_= AsyncEngine, # subclasse de  personalizada de sessionmaker
    bind=engine,
    pool_pre_ping=True, #testando a conexão
    echo=True 

    
)
