import os
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException
from responses.registration import Registration
from models.user_model import User
from payloads.registration import RegistrationPayload
from cryptography.fernet import Fernet
from dotenv import load_dotenv

registration_router = APIRouter(prefix='/registraton', tags=['Регистрация'])

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY
FERNET = Fernet(SECRET_KEY)

@registration_router.post("/", summary="Зарегистрироваться", response_model=Registration)
def make_registration(payload: RegistrationPayload):
    if payload.password != payload.password_retry:
        raise HTTPException(status_code=400, detail="Error: Пароли должны совпадать")

    new_user = User(
        name="Николай",
        email=payload.email,
        password=FERNET.encrypt(payload.password.encode()).decode(),
        card_number="0000000000000000",
        created_at=datetime.now(timezone.utc)
    )

    try:
        new_user.save()
        return {"detail": "OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: Ошибка добавления в базу данных - {str(e)}")