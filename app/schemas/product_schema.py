from pydantic import BaseModel, Field,field_validator
from datetime import datetime
from typing import Optional

class CategoryOut(BaseModel):
    category_id: int
    category_name: str

class StatusOut(BaseModel):
    status_id: int
    status_name: str

class ProductBase(BaseModel):
    product_name : str = Field(...,min_length=2,max_length=100,description="Product Name")
    description : str = Field(...,min_length=4,max_length=500,description="Product Description")
    price : float = Field(...,ge=0,description="Product Price")
    category_id : int = Field(description="Product Category",default=True)
    status_id: int = Field(description="Product Status",default=True)

    @field_validator("product_name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        return value.strip().title()

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    product_id : int
    category :  Optional[CategoryOut] = None
    status : Optional[StatusOut] = None
    created_at : datetime
    updated_at: Optional[datetime] = None

    @field_validator("product_name")
    @classmethod
    def normalize_name(cls, value: Optional[str]) -> Optional[str]:
        return value.strip().title()

class ProductPatch(BaseModel):
    product_name: Optional[str] = Field(min_length=2, max_length=100, description="Product Name")
    description: Optional[str] = Field(min_length=4, max_length=300, description="Product Description")
    price: Optional[float] = Field(ge=0, description="Product Price")
    category_id: Optional[int] = Field(description="Product Category")
    status_id: Optional[int] = Field(description="Product Status")

