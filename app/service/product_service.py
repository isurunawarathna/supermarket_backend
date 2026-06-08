from typing import Optional

from sqlalchemy.orm import Session
from app.repository import ProductsRepository
from app.schemas import ProductCreate, ProductResponse
from fastapi import HTTPException
from starlette import status


class ProductService:

    def __init__(self,repository: ProductsRepository):
        self.products_repository = repository

    def create_product(self,product_data: ProductCreate,db:Session) -> ProductResponse:

        if not product_data.product_name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product Name cannot be empty")

        existing_product = self.products_repository.get_by_name(product_name=product_data.product_name,db=db)

        if existing_product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product already exists")

        return self.products_repository.create_product(product_data=product_data,db=db)

    def get_all_products(self,db:Session):
        return self.products_repository.get_all_products(db=db)

    def get_by_id(self,product_id:int,db:Session)->Optional[ProductResponse]:

        if product_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Product ID")

        return self.products_repository.get_by_id(product_id=product_id,db=db)




