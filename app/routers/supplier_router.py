from typing import Optional
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from starlette import status
from app.schemas import SupplierCreate, SupplierResponse, SupplierPatch
from app.service import SupplierService
from app.repository import SupplierRepository
from sqlalchemy.orm import Session
from app.config import get_db

routers = APIRouter(prefix="/suppliers",tags=["Suppliers"])

supplier_service = SupplierService(repository=SupplierRepository())

@routers.post("/",response_model=SupplierResponse,status_code=status.HTTP_201_CREATED)
def create_supplier(supplier_data:SupplierCreate,db:Session = Depends(get_db)):
    try:
        return supplier_service.create_supplier(supplier_data=supplier_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@routers.get("/",status_code=status.HTTP_302_FOUND)
def get_all_suppliers(db:Session = Depends(get_db)):
    try:
        return supplier_service.get_all_suppliers(db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.get("/{supplier_id}",response_model=Optional[SupplierResponse],status_code=status.HTTP_302_FOUND)
def get_by_id(supplier_id:int, db:Session = Depends(get_db)):
    try:
        return supplier_service.get_by_id(supplier_id=supplier_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.put("/{supplier_id}",response_model=Optional[SupplierResponse],status_code=status.HTTP_200_OK)
def update_supplier(supplier_id:int,supplier_data:SupplierCreate,db:Session = Depends(get_db)):
    try:
        return supplier_service.update_supplier(supplier_data=supplier_data,supplier_id=supplier_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.patch("/{supplier_id}",response_model=Optional[SupplierResponse],status_code=status.HTTP_200_OK)
def patch_supplier(supplier_id:int,supplier_data:SupplierPatch,db: Session = Depends(get_db)):
    try:
        return supplier_service.patch_supplier(supplier_id=supplier_id,supplier_data=supplier_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.delete("/{supplier_id}",response_model=bool,status_code=status.HTTP_200_OK)
def delete_supplier(supplier_id:int,db:Session = Depends(get_db)):
    try:
        return supplier_service.delete_supplier(supplier_id=supplier_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))





