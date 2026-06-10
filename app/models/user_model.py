from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.config import Base

class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    contact_no = Column(String(10),nullable=False)
    email = Column(String(200),unique=True,index=True,nullable=False)
    hash_password = Column(String(255),nullable=False)
    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)
    status_id = Column(Integer, ForeignKey("statuses.status_id"), nullable=False)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now(),onupdate=datetime.now())

    role = relationship("Role", back_populates="users")
    status = relationship("Status", back_populates="users")
    orders = relationship("Orders",back_populates="users")

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"
