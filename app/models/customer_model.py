from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.config import Base

class Customers(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    customer_name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    contact_no = Column(String(10),unique=True,index=True,nullable=False)
    email = Column(String(200),unique=True,index=True,nullable=False)
    address = Column(String(500),nullable=False)
    status_id = Column(Integer, ForeignKey("statuses.status_id"), nullable=False)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now(),onupdate=datetime.now())

    status = relationship("Status", back_populates="customers")

    def __repr__(self):
        return f"<Customer {self.email} ({self.customer_name})>"
