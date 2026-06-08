from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.config import Base

class Category(Base):

    __tablename__ = "categories"

    category_id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    category_name = Column(String(100),nullable=False)

    products = relationship("Products",back_populates="category")
    # inventory = relationship("Inventory",back_populates="category")

    def __repr__(self):
        return f"<Category {self.category_name}>"
