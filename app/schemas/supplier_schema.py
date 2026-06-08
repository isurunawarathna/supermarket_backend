from pydantic import BaseModel, Field,field_validator
from datetime import datetime
from typing import Optional

class StatusOut(BaseModel):
    status_id: int
    status_name: str

class SupplierBase(BaseModel):
    supplier_name : str = Field(...,min_length=3,max_length=100,description="Supplier Name")
    age : int = Field(...,ge=0,description="Supplier age")
    status_id : int = Field(description="Supplier Status",default=True)
    contact_no : str = Field(...,pattern=r'^(?:\+94|94|0)?(?:7[01245678]\d|11\d|21\d|23\d|24\d|25\d|26\d|27\d|31\d|32\d|33\d|34\d|35\d|36\d|37\d|38\d|41\d|45\d|47\d|51\d|52\d|54\d|55\d|57\d|63\d|65\d|66\d|67\d|81\d|91\d)\d{6}$')
    email : str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',description="User Email Address")
    company_name : str = Field(...,description="Supplier Company Name")

    @field_validator("email")
    @classmethod
    def validate_email(cls,value:str) -> str:
        return value.lower()

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    supplier_id: int
    status: Optional[StatusOut] = None
    created_at :datetime
    updated_at : Optional[datetime] = None

class SupplierPatch(BaseModel):
    supplier_name: Optional[str] = Field(min_length=3, max_length=100, description="Supplier Name")
    age: Optional[int] = Field(ge=0, description="Supplier age")
    contact_no: Optional[str] = Field(pattern=r'^(?:\+94|94|0)?(?:7[01245678]\d|11\d|21\d|23\d|24\d|25\d|26\d|27\d|31\d|32\d|33\d|34\d|35\d|36\d|37\d|38\d|41\d|45\d|47\d|51\d|52\d|54\d|55\d|57\d|63\d|65\d|66\d|67\d|81\d|91\d)\d{6}$')
    status_id: Optional[int] = Field(description="Supplier Status",default=True)
    email: Optional[str] = Field(pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',description="Supplier Email Address")
    company_name : Optional[str] = Field(min_length=4,max_length=100,description="Supplier Company Name")

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return value.lower()