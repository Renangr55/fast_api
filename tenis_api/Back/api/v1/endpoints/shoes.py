from typing import List
from fastapi import (
    APIRouter, 
    status, 
    Depends,
    HTTPException, 
    Response)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.shoes_model import ShoesModel
from schemas.shoes_schemas import ShoesSchemas

from core.deps import get_session

router = APIRouter()

# create
@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=ShoesSchemas)
async def created_shoes(shoes:ShoesSchemas, db: AsyncSession = Depends(get_session)):
    new_shoes = ShoesModel(name=shoes.name, brand=shoes.brand,price=shoes.price, gender=shoes.gender, numbering=shoes.numbering, color=shoes.color, description=shoes.description)
    
    db.add(new_shoes)
    await db.commit()
    
    return shoes

# read
@router.get("list/", response_model=list[ShoesSchemas])
async def get_shoes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ShoesModel)
        result = await session.execute(query)
        shoes: List[ShoesModel] = result.scalars().all()
        
        return shoes
    
#read with id
@router.get("list/{shoes_id}",status_code=status.HTTP_200_OK, response_model=ShoesSchemas)
async def get_shoes(shoes_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ShoesModel).filter(ShoesModel.id == shoes_id)
        result = await session.execute(query)
        shoes = result.scalar_one_or_none()
        
        if shoes:
            return shoes
        else:
            raise HTTPException(detail="Shoes not found", status_code=status.HTTP_404_NOT_FOUND)
    
#put
@router.put("update/{shoes_id}", status_code=status.HTTP_202_ACCEPTED, response_model=ShoesSchemas)
async def put_shoes(shoes_id: int, shoes: ShoesSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ShoesModel).filter(ShoesModel.id == shoes_id)
        result = await session.execute(query)
        shoes_up = result.scalar_one_or_none()
        
        if shoes_up:
            
            shoes_up.brand = shoes.brand
            shoes_up.gender = shoes.gender
            shoes_up.color = shoes.color
            shoes_up.numbering = shoes.numbering
            
            await session.commit()
            
            return shoes_up 
        else:
            raise HTTPException(detail="shoes not found", status_code=status.HTTP_404_NOT_FOUND)
        
        
#delete       
@router.delete("delete/{shoes_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_shoes(shoes_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ShoesModel).filter(ShoesModel.id == shoes_id)
        result = await session.execute(query)
        shoes_del = result.scalar_one_or_none()
        if shoes_del:
            await session.delete(shoes_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="shoes not found", status_code=status.HTTP_404_NOT_FOUND)
    

    
