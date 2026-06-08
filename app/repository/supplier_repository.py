from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session,joinedload
from app.models import Supplier
from app.schemas import SupplierCreate, SupplierResponse,SupplierPatch


class SupplierRepository:

    @staticmethod
    def create_supplier(supplier_data:SupplierCreate,db:Session) -> SupplierResponse:

        new_supplier = Supplier(
            supplier_name=supplier_data.supplier_name,
            age=supplier_data.age,
            contact_no=supplier_data.contact_no,
            email=supplier_data.email,
            company_name=supplier_data.company_name,
            status_id=supplier_data.status_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        db.add(new_supplier)
        db.commit()
        db.refresh(new_supplier)
        return new_supplier

    @staticmethod
    def get_all_supplier(db:Session):
        return db.query(Supplier).options(joinedload(Supplier.status)).all()

    @staticmethod
    def get_by_id(supplier_id:int, db:Session) -> Optional[SupplierResponse]:
        return db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

    @staticmethod
    def get_by_email(email:str,db:Session)->Optional[SupplierResponse]:
        return db.query(Supplier).filter(Supplier.email == email).first()

    @staticmethod
    def update_supplier(supplier_id:int,supplier_data:SupplierCreate,db:Session) -> Optional[SupplierResponse]:
        db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

        db_supplier.supplier_name = supplier_data.supplier_name
        db_supplier.age = supplier_data.age
        db_supplier.contact_no = supplier_data.contact_no
        db_supplier.email = supplier_data.email
        db_supplier.company_name = supplier_data.company_name
        db_supplier.status_id = supplier_data.status_id

        db.commit()
        db.refresh(db_supplier)
        return db_supplier

    @staticmethod
    def patch_supplier(supplier_id:int,supplier_data:SupplierPatch,db:Session) -> Optional[SupplierResponse]:

        existing_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

        update_data = supplier_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(existing_supplier, key, value)

        db.commit()
        db.refresh(existing_supplier)

        return existing_supplier

    @staticmethod
    def delete_supplier(supplier_id:int,db:Session)->bool:
        db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()

        if not db_supplier:
            return False

        db.delete(db_supplier)
        db.commit()
        return True



















