from fastapi import Depends,HTTPException
from starlette import status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.schemas import UserResponse
from app.config import get_db,decode_access_token
from app.models import User

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):

    token = credentials.credentials

    payload = decode_access_token(token=token)

    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token payload")

    user = db.query(User).filter(User.user_id == int(user_id)).first() ##small upgrade needed in here

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")

    return user

def require_role(*role_ids:int):
    def check_role(current_user: UserResponse = Depends(get_current_user)):
        if current_user.role_id is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Role not Assigned")

        if current_user.role_id not in role_ids:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Insufficient Permission")

        return current_user
    return check_role


require_admin = require_role(1)


