from core.configs import settings
from core.database import engine
from models import all_models

async def create_tables() -> None:
    print("Created tables in database")
    
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("sucessfull!! tables createds")
    
if __name__ == '__main__':
    import asyncio
    
    asyncio.run(create_tables())  