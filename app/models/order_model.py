# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Double
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.config import Base
#
#
# class Orders(Base):
#
#     __tablename__ = "orders"
#
#     order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
#     status_id = Column(Integer, ForeignKey("statuses.status_id"), nullable=False)
#     total_amount = Column(Double, nullable=False)
#     notes = Column(String(500), unique=True, nullable=True)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#
#     user = relationship("User", back_populates="orders")
#     status = relationship("Status", back_populates="orders")
#     order_items = relationship("OrderItems", back_populates="orders")
#     payments = relationship("Payments", back_populates="orders")
#
#     def __repr__(self):
#         return f"<Orders {self.order_id} - User {self.user_id}>"