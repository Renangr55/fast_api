from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title="Shoes API - fastapi Sqlite")
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def teste():
    return {"Deu certo", "teste"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True) #log level é um sistema de registros do funcionamento da api
