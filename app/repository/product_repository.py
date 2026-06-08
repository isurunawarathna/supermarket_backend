from typing import Optional
from sqlalchemy.orm import Session
from app.schemas import ProductCreate, ProductResponse
from app.models import Products
from datetime import datetime

class ProductsRepository:

    @staticmethod
    def create_product(product_data:ProductCreate,db:Session) -> ProductResponse:
        new_product = Products(
             product_name=product_data.product_name,
             description=product_data.description,
             price=product_data.price,
             category_id=product_data.category_id,
             status_id=product_data.status_id,
             created_at=datetime.now(),
             updated_at=datetime.now()
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product

    @staticmethod
    def get_all_products(db:Session):
        return db.query(Products).all()

    @staticmethod
    def get_by_id(product_id:int,db:Session) -> Optional[ProductResponse]:
        return db.query(Products).filter(Products.product_id == product_id).first()

    @staticmethod
    def get_by_name(product_name:str,db:Session) -> Optional[ProductResponse]:
        return db.query(Products).filter(Products.product_name == product_name).first()
