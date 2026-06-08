from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class OrderOut(BaseModel):
    order_id: int

    model_config = ConfigDict(from_attributes=True)

class PaymentMethodOut(BaseModel):
    method_id: int
    method_name: str

    model_config = ConfigDict(from_attributes=True)

class StatusOut(BaseModel):
    status_id: int
    status_name: str

    model_config = ConfigDict(from_attributes=True)

class PaymentBase(BaseModel):
    order_id: int = Field(..., description="Order ID")
    payment_method_id: int = Field(..., description="Payment Method ID")
    payment_status_id: int = Field(..., description="Payment Status ID")
    amount: float = Field(..., gt=0, description="Payment Amount")

    transaction_reference: Optional[str] = Field(None,max_length=500,description="Unique transaction reference")

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    order: Optional[OrderOut] = None
    payment_methods: Optional[PaymentMethodOut] = None
    status: Optional[StatusOut] = None

    model_config = ConfigDict(from_attributes=True)

class PaymentPatch(BaseModel):
    order_id: Optional[int] = None
    payment_method_id: Optional[int] = None
    payment_status_id: Optional[int] = None
    amount: Optional[float] = Field(None, gt=0)
    transaction_reference: Optional[str] = Field(None, max_length=500)