from subscriptions.schemas import SubscriptionCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from core.database import get_db
from subscriptions.models import Subscription

router = APIRouter()

@router.post('/subscriptions')
def create_subscription(newSubscription: SubscriptionCreate, session: Session = Depends(get_db)):
    db_subscription = Subscription(**newSubscription.model_dump())
    session.add(db_subscription)
    session.commit()
    session.refresh(db_subscription)
    return db_subscription