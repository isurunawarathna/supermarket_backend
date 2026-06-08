# from sqlalchemy import Column, Integer, String, DateTime, Boolean
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from app.config import Base
#
#
# class PaymentMethod(Base):
#
#     __tablename__ = "payment_methods"
#
#     method_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     method_name = Column(String(100), nullable=False, unique=True)
#     created_at = Column(DateTime, default=datetime.now())
#     updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
#
#     payments = relationship("Payments", back_populates="payment_methods")
#
#     def __repr__(self):
#         return f"<PaymentMethod {self.method_name}>"