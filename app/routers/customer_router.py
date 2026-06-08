from typing import Optional
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from starlette import status
from app.schemas import CustomerCreate, CustomerResponse, CustomerPatch
from app.service import CustomerService
from app.repository import CustomerRepository
from sqlalchemy.orm import Session
from app.config import get_db

routers = APIRouter(prefix="/customers",tags=["Customers"])

customer_service = CustomerService(repository=CustomerRepository())

@routers.post("/",response_model=CustomerResponse,status_code=status.HTTP_201_CREATED)
def create_customer(customer_data:CustomerCreate,db:Session = Depends(get_db)):
    try:
        return customer_service.create_customer(customer_data=customer_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@routers.get("/",status_code=status.HTTP_302_FOUND)
def get_all_customers(db:Session = Depends(get_db)):
    try:
        return customer_service.get_all_customers(db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.get("/{customer_id}",response_model=Optional[CustomerResponse],status_code=status.HTTP_302_FOUND)
def get_by_id(customer_id:int, db:Session = Depends(get_db)):
    try:
        return customer_service.get_by_id(customer_id=customer_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.put("/{customer_id}",response_model=Optional[CustomerResponse],status_code=status.HTTP_200_OK)
def update_customer(customer_id:int,customer_data:CustomerCreate,db:Session = Depends(get_db)):
    try:
        return customer_service.update_customer(customer_data=customer_data,customer_id=customer_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.patch("/{customer_id}",response_model=Optional[CustomerResponse],status_code=status.HTTP_200_OK)
def patch_customer(customer_id:int,customer_data:CustomerPatch,db: Session = Depends(get_db)):
    try:
        return customer_service.patch_customer(customer_id=customer_id,customer_data=customer_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.delete("/{customer_id}",response_model=bool,status_code=status.HTTP_200_OK)
def delete_customer(customer_id:int,db:Session = Depends(get_db)):
    try:
        return customer_service.delete_customer(customer_id=customer_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))





