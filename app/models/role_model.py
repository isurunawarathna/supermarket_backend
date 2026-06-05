from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(50), unique=True, nullable=False)

    # Relationship
    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"