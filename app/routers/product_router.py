from typing import Optional

from sqlalchemy.orm import Session
from app.schemas import ProductCreate,ProductResponse
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from app.config import get_db
from app.repository import ProductsRepository
from app.service import ProductService

routers = APIRouter(prefix="/products",tags=["Products"])

product_service = ProductService(repository=ProductsRepository())

@routers.post("/",response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(product_data:ProductCreate,db:Session = Depends(get_db)):
    try:
        return product_service.create_product(product_data=product_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@routers.get("/",status_code=status.HTTP_302_FOUND)
def get_all_products(db:Session = Depends(get_db)):
    try:
        return product_service.get_all_products(db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.get("/{product_id}",response_model=Optional[ProductResponse],status_code=status.HTTP_302_FOUND)
def get_by_id(product_id:int,db:Session = Depends(get_db)):
    try:
        return product_service.get_by_id(product_id=product_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))


