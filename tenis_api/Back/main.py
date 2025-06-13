from fastapi import FastAPI
from core.configs import settings
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router


app = FastAPI(title="Shoes API - fastapi Sqlite")
app.include_router(api_router, prefix=settings.API_V1_STR)
origins = ["http://localhost","http://localhost:3000"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"])

@app.get("/")
async def teste():
    return {"Deu certo", "teste"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True) #log level é um sistema de registros do funcionamento da api
