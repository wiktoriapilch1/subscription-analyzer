from core.database import Base
from sqlalchemy import Column, Integer, String, Date

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Integer)
    user_email = Column(String)
    purchase_date = Column(Date)
    due_date = Column(Date)
    billing_cycle = Column(String)