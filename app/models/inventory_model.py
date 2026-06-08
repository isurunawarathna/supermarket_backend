# from sqlalchemy import Column, Integer, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.config import Base
#
#
# class Inventory(Base):
#
#     __tablename__ = "inventory"
#
#     inventory_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
#     category_id = Column(Integer,ForeignKey("categories.category_id"),nullable=False)
#     stock_quantity = Column(Integer, nullable=False, default=0)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#
#     product = relationship("Products", back_populates="inventory")
#     category = relationship("Category",back_populates="inventory")
#
#     def available_stock(self):
#         return self.stock_quantity - self.reserved_quantity
#
#     def __repr__(self):
#         return f"<Inventory Product:{self.product_id} Stock:{self.stock_quantity}>"