from typing import Optional
from sqlalchemy.orm import Session,joinedload
from app.models import User
from app.schemas import UserResponse, UserCreate, UserPatch
from app.config import hash_password


class UserRepository:

    @staticmethod
    def create_user(user_data:UserCreate,db:Session) -> UserResponse:

        hashed_password = hash_password(user_data.password)

        new_user = User(
            name=user_data.name,
            age=user_data.age,
            contact_no=user_data.contact_no,
            email=user_data.email,
            hash_password=hashed_password,
            role_id=user_data.role_id,
            status_id=user_data.status_id
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_all_users(db:Session):
        return db.query(User).options(joinedload(User.status),joinedload(User.role)).all()

    @staticmethod
    def get_by_id(user_id:int, db:Session) -> Optional[UserResponse]:
        return db.query(User).filter(User.user_id == user_id).first()

    @staticmethod
    def get_by_email(email:str,db:Session)->Optional[UserResponse]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def update_user(user_id:int,user_data:UserCreate,db:Session)->Optional[UserResponse]:
        db_user = db.query(User).filter(User.user_id == user_id).first()

        db_user.name = user_data.name
        db_user.age = user_data.age
        db_user.contact_no = user_data.contact_no
        db_user.email = user_data.email
        db_user.hash_password = hash_password(password=user_data.password)
        db_user.role_id = user_data.role_id
        db_user.status_id = user_data.status_id

        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def patch_user(user_id:int,user_data:UserPatch,db:Session) -> Optional[UserResponse]:

        existing_user = db.query(User).filter(User.user_id == user_id).first()

        update_data = user_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(existing_user, key, value)

        db.commit()
        db.refresh(existing_user)

        return existing_user

    @staticmethod
    def delete_user(user_id:int,db:Session)->bool:
        db_user = db.query(User).filter(User.user_id == user_id).first()

        if not db_user:
            return False

        db.delete(db_user)
        db.commit()
        return True



















