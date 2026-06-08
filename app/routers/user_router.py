from typing import Optional
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from starlette import status
from app.schemas import UserCreate, UserResponse, UserPatch
from app.service import UserService
from app.repository import UserRepository
from sqlalchemy.orm import Session
from app.config import get_db
from app.middleware import require_admin

routers = APIRouter(prefix="/users",tags=["Users"])

user_service = UserService(repository=UserRepository())

@routers.post("/",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_users(user_data:UserCreate,db:Session = Depends(get_db),current_user:UserResponse = Depends(require_admin)):
    try:
        return user_service.create_user(user_data=user_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=str(e))

@routers.get("/",status_code=status.HTTP_302_FOUND)
def get_all_users(db:Session = Depends(get_db)):
    try:
        return user_service.get_all_users(db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.get("/{user_id}",response_model=Optional[UserResponse],status_code=status.HTTP_302_FOUND)
def get_by_id(user_id:int, db:Session = Depends(get_db)):
    try:
        return user_service.get_by_id(user_id=user_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.put("/{user_id}",response_model=Optional[UserResponse],status_code=status.HTTP_200_OK)
def update_user(user_id:int,user_data:UserCreate,db:Session = Depends(get_db)):
    try:
        return user_service.update_user(user_data=user_data,user_id=user_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.patch("/{user_id}",response_model=Optional[UserResponse],status_code=status.HTTP_200_OK)
def patch_user(user_id:int,user_data:UserPatch,db: Session = Depends(get_db)):
    try:
        return user_service.patch_user(user_id=user_id,user_data=user_data,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))

@routers.delete("/{user_id}",response_model=bool,status_code=status.HTTP_200_OK)
def delete_user(user_id:int,db:Session = Depends(get_db)):
    try:
        return user_service.delete_user(user_id=user_id,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))





