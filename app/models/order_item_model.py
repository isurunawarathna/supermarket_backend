# from sqlalchemy import Column, Integer, ForeignKey, Double, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.config import Base
#
#
# class OrderItems(Base):
#
#     __tablename__ = "order_items"
#
#     order_item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
#     quantity = Column(Integer, nullable=False)
#     unit_price = Column(Double, nullable=False)
#     total_price = Column(Double, nullable=False)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#
#     order = relationship("Orders", back_populates="order_items")
#     product = relationship("Products",back_populates="order_items")
#
#     def __repr__(self):
#         return f"<OrderItems Order:{self.order_id} Product:{self.product_id} Qty:{self.quantity}>"