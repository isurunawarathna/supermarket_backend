# from sqlalchemy import Column, Integer, String, ForeignKey, Double, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.config import Base
#
#
# class Payments(Base):
#
#     __tablename__ = "payments"
#
#     payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
#     payment_method_id = Column(Integer,ForeignKey("payment_methods.method_id"), nullable=False)
#     payment_status_id = Column(Integer,ForeignKey("statuses.status_id"), nullable=False)
#     amount = Column(Double, nullable=False)
#     transaction_reference = Column(String(150), unique=True, nullable=True)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#
#     order = relationship("Orders", back_populates="payments")
#     payment_methods = relationship("PaymentMethod",back_populates="payments")
#     status = relationship("Status",back_populates="payments")
#
#     def __repr__(self):
#         return f"<Payments Order:{self.order_id} Status:{self.payment_status}>"