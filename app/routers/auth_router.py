from fastapi import APIRouter,Depends,HTTPException
from app.schemas import LoginRequest, UserResponse
from starlette import status
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import UserService
from app.repository import UserRepository
from app.middleware import get_current_user,require_admin

routers = APIRouter(prefix="/auth",tags=["Authentications"])

user_service = UserService(repository=UserRepository())

@routers.post("/login",status_code=status.HTTP_200_OK)
def login_user(request:LoginRequest,db: Session = Depends(get_db)):
    try:
        return user_service.authenticate(request=request,db=db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))

@routers.get("/me",status_code=status.HTTP_200_OK)
def get_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user.user_id


