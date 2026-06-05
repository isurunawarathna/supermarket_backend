from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config import Base


class Status(Base):
    __tablename__ = "statuses"

    status_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status_name = Column(String(50), unique=True, nullable=False)

    # Relationship
    users = relationship("User", back_populates="status")

    def __repr__(self):
        return f"<Status {self.name}>"