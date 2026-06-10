from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base


class Status(Base):
    __tablename__ = "statuses"

    status_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status_name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="status")
    products = relationship("Products",back_populates="status")
    suppliers = relationship("Supplier", back_populates="status")
    customers = relationship("Customers",back_populates="status")
    orders = relationship("Orders",back_populates="status")
    # payments = relationship("Payments",back_populates="status")



    def __repr__(self):
        return f"<Status {self.status_name}>"