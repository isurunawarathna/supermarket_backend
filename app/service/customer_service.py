from sqlalchemy.orm import Session
from app.repository import CustomerRepository
from app.schemas import CustomerCreate, CustomerResponse, CustomerPatch
from typing import Optional
from fastapi import HTTPException
from starlette import status

class CustomerService:

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create_customer(self, customer_data:CustomerCreate,db: Session) -> CustomerResponse:

        if customer_data.age < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Age")

        if not customer_data.customer_name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Name cannot be empty")

        existing_customer = self.repository.get_by_email(email=customer_data.email,db=db)

        if existing_customer:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Customer already exists")

        return self.repository.create_customer(customer_data=customer_data,db=db)

    def get_all_customers(self,db:Session):
        return self.repository.get_all_customer(db=db)

    def get_by_id(self,customer_id:int,db:Session) -> Optional[CustomerResponse]:

        if customer_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.get_by_id(customer_id=customer_id,db=db)


    def update_customer(self, customer_id:int,db:Session, customer_data:CustomerCreate)->Optional[CustomerResponse]:

        if  customer_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid customer ID")

        return self.repository.update_customer(customer_id= customer_id, customer_data= customer_data,db=db)

    def patch_customer(self, customer_id:int, customer_data: CustomerPatch,db:Session):

        if  customer_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid customer ID")

        return self.repository.patch_customer(customer_id=customer_id, customer_data=customer_data,db=db)

    def delete_customer(self, customer_id:int,db:Session)->bool:

        if customer_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid customer ID")

        return self.repository.delete_customer(customer_id=customer_id,db=db)






