from sqlalchemy.orm import Session
from app.repository import SupplierRepository
from app.schemas import SupplierCreate, SupplierResponse, SupplierPatch
from typing import Optional
from fastapi import HTTPException
from starlette import status

class SupplierService:

    def __init__(self, repository: SupplierRepository):
        self.repository = repository

    def create_supplier(self, supplier_data:SupplierCreate,db: Session) -> SupplierResponse:

        if supplier_data.age < 0 or supplier_data.age > 60:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Age must be between 0 and 60")

        if not supplier_data.supplier_name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Name cannot be empty")

        existing_supplier = self.repository.get_by_email(email=supplier_data.email,db=db)

        if existing_supplier:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")

        return self.repository.create_supplier(supplier_data=supplier_data,db=db)

    def get_all_suppliers(self,db:Session):
        return self.repository.get_all_supplier(db=db)

    def get_by_id(self,supplier_id:int,db:Session) -> Optional[SupplierResponse]:

        if supplier_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.get_by_id(supplier_id=supplier_id,db=db)


    def update_supplier(self,supplier_id:int,db:Session,supplier_data:SupplierCreate)->Optional[SupplierResponse]:

        if supplier_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.update_supplier(supplier_id=supplier_id,supplier_data=supplier_data,db=db)

    def patch_supplier(self,supplier_id:int,supplier_data: SupplierPatch,db:Session):

        if supplier_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.patch_supplier(supplier_id=supplier_id,supplier_data=supplier_data,db=db)

    def delete_supplier(self,supplier_id:int,db:Session)->bool:

        if supplier_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.delete_supplier(supplier_id=supplier_id,db=db)






