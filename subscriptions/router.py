from fastapi import Depends, HTTPException
from fastapi import APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import select

from subscriptions.schemas import SubscriptionCreate
from subscriptions.models import Subscription

from core.database import get_db

router = APIRouter()

@router.post('/subscriptions')
def create_subscription(newSubscription: SubscriptionCreate, session: Session = Depends(get_db)):
    db_subscription = Subscription(**newSubscription.model_dump())
    session.add(db_subscription)
    session.commit()
    session.refresh(db_subscription)
    return db_subscription

@router.get('/subscriptions')
def get_subscriptin(session: Session = Depends(get_db)):
    stmt = select(Subscription)
    subsriptions = session.execute(stmt).scalars().all()
    return subsriptions

@router.get('/subscriptions/{subscription_id}')
def get_subscription_with_id(subscription_id: int, session: Session = Depends(get_db)):
    subscription = session.get(Subscription, subscription_id)
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription