from  typing import Generator
from  sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session
from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]: #Criando um gerador asyc
    session: AsyncSession = Session() 
    try:
        yield session #aqui temos o controle total da session,obeservamos que depois ela fecha ai o yield pausa a função,mais quando executamos ela volta
    finally:
        await session.close() 