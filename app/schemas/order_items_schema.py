from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ProductOut(BaseModel):
    product_id: int
    product_name: str
    price: float

    model_config = ConfigDict(from_attributes=True)


class OrderOut(BaseModel):
    order_id: int

    model_config = ConfigDict(from_attributes=True)

class OrderItemBase(BaseModel):
    order_id: int = Field(..., description="Order ID")
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")
    unit_price: float = Field(..., gt=0, description="Price per unit")
    total_price: float = Field(..., gt=0, description="Total price (quantity * unit_price)")

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    order_item_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    order: Optional[OrderOut] = None
    product: Optional[ProductOut] = None

    model_config = ConfigDict(from_attributes=True)

class OrderItemPatch(BaseModel):
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = Field(None, gt=0)
    unit_price: Optional[float] = Field(None, gt=0)
    total_price: Optional[float] = Field(None, gt=0)