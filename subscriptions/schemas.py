from enum import Enum

from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

from datetime import date

class BillingCycle(str, Enum):
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

class SubscriptionCreate(BaseModel):
    name: str
    amount: int = Field(gt=0)
    user_email: EmailStr
    purchase_date: date
    due_date: date
    billing_cycle: BillingCycle

    @field_validator('due_date')
    @classmethod
    def check_due_date(cls, newDate: date):
        if newDate < date.today():
            raise ValueError("Due date cannot be in the past")
        return newDate
    
    @model_validator(mode='after')
    def check_dates(self) -> 'SubscriptionCreate':
        if self.due_date < self.purchase_date:
            raise ValueError("Due date cannot be earlier than the purchase date")
        return self
    
class SubscriptionUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[int] = None
    user_email: Optional[EmailStr] = None
    purchase_date: Optional[date] = None
    due_date: Optional[date] = None
    billing_cycle: Optional[BillingCycle] = None

    @field_validator('due_date')
    @classmethod
    def check_due_date(cls, newDate: date | None):
        if newDate is not None and newDate < date.today():
            raise ValueError("Due date cannot be in the past")
        return newDate
    
    @model_validator(mode='after')
    def check_dates(self) -> 'SubscriptionCreate':
        if self.due_date is not None and self.purchase_date is not None:
            if self.due_date < self.purchase_date:
                raise ValueError("Due date cannot be earlier than the purchase date")
        return self