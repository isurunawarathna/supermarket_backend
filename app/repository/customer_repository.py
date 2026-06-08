from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session,joinedload
from app.models import Customers
from app.schemas import CustomerCreate,CustomerResponse,CustomerPatch


class CustomerRepository:

    @staticmethod
    def create_customer(customer_data:CustomerCreate,db:Session) -> CustomerResponse:

        new_customer = Customers(
            customer_name=customer_data.customer_name,
            age=customer_data.age,
            contact_no=customer_data.contact_no,
            email=customer_data.email,
            address=customer_data.address,
            status_id=customer_data.status_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer

    @staticmethod
    def get_all_customer(db:Session):
        return db.query(Customers).options(joinedload(Customers.status)).all()

    @staticmethod
    def get_by_id(customer_id:int, db:Session) -> Optional[CustomerResponse]:
        return db.query(Customers).filter(Customers.customer_id == customer_id).first()

    @staticmethod
    def get_by_email(email:str,db:Session)->Optional[CustomerResponse]:
        return db.query(Customers).filter(Customers.email == email).first()

    @staticmethod
    def update_customer(customer_id:int,customer_data:CustomerCreate,db:Session) -> Optional[CustomerResponse]:
        db_customer = db.query(Customers).filter(Customers.customer_id == customer_id).first()

        db_customer.customer_name = customer_data.customer_name
        db_customer.age = customer_data.age
        db_customer.contact_no = customer_data.contact_no
        db_customer.email = customer_data.email
        db_customer.address = customer_data.address
        db_customer.status_id = customer_data.status_id

        db.commit()
        db.refresh(db_customer)
        return db_customer

    @staticmethod
    def patch_customer(customer_id:int,customer_data:CustomerPatch,db:Session) -> Optional[CustomerResponse]:

        existing_customer = db.query(Customers).filter(Customers.customer_id == customer_id).first()

        update_data = customer_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(existing_customer, key, value)

        db.commit()
        db.refresh(existing_customer)

        return existing_customer

    @staticmethod
    def delete_customer(customer_id:int,db:Session)->bool:
        db_customer = db.query(Customers).filter(Customers.customer_id == customer_id).first()

        if not db_customer:
            return False

        db.delete(db_customer)
        db.commit()
        return True



















