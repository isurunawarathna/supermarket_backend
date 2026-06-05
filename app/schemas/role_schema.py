from pydantic import BaseModel


class RoleBase(BaseModel):
    role_name: str


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    role_id: int

