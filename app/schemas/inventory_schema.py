from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ProductOut(BaseModel):
    product_id: int
    product_name: str

    model_config = ConfigDict(from_attributes=True)


class CategoryOut(BaseModel):
    category_id: int
    category_name: str

    model_config = ConfigDict(from_attributes=True)

class InventoryBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    category_id: int = Field(..., description="Category ID")
    stock_quantity: int = Field(..., ge=0, description="Available stock quantity")

class InventoryCreate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    inventory_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    product: Optional[ProductOut] = None
    category: Optional[CategoryOut] = None

    model_config = ConfigDict(from_attributes=True)

class InventoryPatch(BaseModel):
    product_id: Optional[int] = None
    category_id: Optional[int] = None
    stock_quantity: Optional[int] = Field(None, ge=0)