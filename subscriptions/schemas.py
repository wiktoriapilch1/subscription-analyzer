from enum import Enum

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
            raise ValueError("Due date cannot be eralier than the purchase date")
        return self