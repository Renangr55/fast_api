from fastapi import APIRouter
from api.v1.endpoints import shoes

api_router = APIRouter()
api_router.include_router(shoes.router, prefix="shoes/", tags=["shoes"])
#/api/v1/shoes -> esse será nosso endpoint completo junto ao prefixo!
