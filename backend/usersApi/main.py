from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import user_router

app = FastAPI(
    title="User Service",
    root_path="/userservice",
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

app.include_router(user_router)