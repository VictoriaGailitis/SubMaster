from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.subscriptions import subscription_router

app = FastAPI(
    title="Subscription Service",
    root_path="/subscriptionservice",
    redirect_slashes=False
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subscription_router)