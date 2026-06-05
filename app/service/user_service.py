from sqlalchemy.orm import Session
from app.repository import UserRepository
from app.schemas import UserCreate, UserResponse, UserPatch
from typing import Optional
from fastapi import HTTPException
from starlette import status

class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user_data:UserCreate,db: Session) -> UserResponse:

        if user_data.age < 0 or user_data.age > 60:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Age must be between 0 and 60")

        if not user_data.name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Name cannot be empty")

        existing_user = self.repository.get_by_email(email=user_data.email,db=db)

        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")

        return self.repository.create_user(user_data=user_data,db=db)

    def get_all_users(self,db:Session):
        return self.repository.get_all_users(db=db)

    def get_by_id(self,user_id:int,db:Session) -> Optional[UserResponse]:

        if user_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.get_by_id(user_id=user_id,db=db)


    def update_user(self,user_id:int,db:Session,user_data:UserCreate)->Optional[UserResponse]:

        if user_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.update_user(user_id=user_id,user_data=user_data,db=db)

    def patch_user(self,user_id:int,user_data: UserPatch,db:Session):

        if user_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.patch_user(user_id=user_id,user_data=user_data,db=db)

    def delete_user(self,user_id:int,db:Session)->bool:

        if user_id <=0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid user ID")

        return self.repository.delete_user(user_id=user_id,db=db)






