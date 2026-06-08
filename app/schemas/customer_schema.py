from pydantic import BaseModel, Field,field_validator
from datetime import datetime
from typing import Optional

class StatusOut(BaseModel):
    status_id: int
    status_name: str

class CustomerBase(BaseModel):
    customer_name : str = Field(...,min_length=3,max_length=100,description="Customer Name")
    age : int = Field(...,ge=0,description="Customer Age")
    status_id : int = Field(description="Customer Status",default=True)
    contact_no : str = Field(...,pattern=r'^(?:\+94|94|0)?(?:7[01245678]\d|11\d|21\d|23\d|24\d|25\d|26\d|27\d|31\d|32\d|33\d|34\d|35\d|36\d|37\d|38\d|41\d|45\d|47\d|51\d|52\d|54\d|55\d|57\d|63\d|65\d|66\d|67\d|81\d|91\d)\d{6}$')
    email : str = Field(...,pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',description="Customer Email Address")
    address : str = Field(...,min_length=4,max_length=500,description="Customer Address")


    @field_validator("email")
    @classmethod
    def validate_email(cls,value:str) -> str:
        return value.lower()

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    customer_id: int
    status: StatusOut
    created_at :datetime
    updated_at : Optional[datetime] = None

class CustomerPatch(BaseModel):
    customer_name: Optional[str] = Field(min_length=3, max_length=100, description="Customer Name")
    age: Optional[int] = Field(ge=0, description="Customer age")
    contact_no: Optional[str] = Field(pattern=r'^(?:\+94|94|0)?(?:7[01245678]\d|11\d|21\d|23\d|24\d|25\d|26\d|27\d|31\d|32\d|33\d|34\d|35\d|36\d|37\d|38\d|41\d|45\d|47\d|51\d|52\d|54\d|55\d|57\d|63\d|65\d|66\d|67\d|81\d|91\d)\d{6}$')
    status_id: Optional[int] = Field(description="Customer Status",default=True)
    email: Optional[str] = Field(pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',description="Customer Email Address")
    address : Optional[str] = Field(min_length=4,max_length=500,description="Customer Address")

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return value.lower()