from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional, List

class UserOut(BaseModel):
    user_id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class StatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)

class OrderItemOut(BaseModel):
    order_item_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_price: float

    model_config = ConfigDict(from_attributes=True)

class PaymentOut(BaseModel):
    payment_id: int
    amount: float
    payment_status_id: int

    model_config = ConfigDict(from_attributes=True)

class OrderBase(BaseModel):
    user_id: int = Field(..., description="User ID who placed the order")
    status_id: int = Field(..., description="Order Status ID")
    total_amount: float = Field(..., gt=0, description="Total order amount")
    notes: Optional[str] = Field(None, max_length=500, description="Optional order notes")

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    order_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    user: Optional[UserOut] = None
    status: Optional[StatusOut] = None
    order_items: Optional[List[OrderItemOut]] = None
    payments: Optional[List[PaymentOut]] = None

    model_config = ConfigDict(from_attributes=True)

class OrderPatch(BaseModel):
    user_id: Optional[int] = None
    status_id: Optional[int] = None
    total_amount: Optional[float] = Field(None, gt=0)
    notes: Optional[str] = Field(None, max_length=500)