from fastapi import FastAPI
from subscriptions.router import router

app = FastAPI()
app.include_router(router)