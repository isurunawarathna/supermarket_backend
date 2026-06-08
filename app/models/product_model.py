from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Double
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from app.config import Base

class Products(Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    product_name = Column(String(200),nullable=False)
    description = Column(String(500),nullable=False)
    price = Column(Double, nullable=False)
    category_id = Column(Integer,ForeignKey("categories.category_id"),nullable=False)
    status_id = Column(Integer,ForeignKey("statuses.status_id"),nullable=False)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now(),onupdate=datetime.now())

    category = relationship("Category",back_populates="products")
    status = relationship("Status",back_populates="products")
    # inventory = relationship("Inventory", back_populates="product", uselist=False)

    def __repr__(self):
        return f"<Products {self.product_name}>"
