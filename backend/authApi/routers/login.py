import os
from cryptography.fernet import Fernet
from fastapi import APIRouter, HTTPException
from responses.login import Login
from models.user_model import User
from payloads.login import LoginPayload
from dotenv import load_dotenv

login_router = APIRouter(prefix='/login', tags=['Вход'])

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
assert SECRET_KEY
FERNET = Fernet(SECRET_KEY)

@login_router.post("/", summary="Войти в систему", response_model=Login)
def make_login(payload: LoginPayload):
    try:
        user = User.get(User.email == payload.email)
    except:
        raise HTTPException(status_code=400, detail="Error: Пользователь не найден")

    try:
        if FERNET.decrypt(user.password.encode()).decode() != payload.password:
            raise HTTPException(status_code=400, detail="Error: Неверный пароль")

        return {
            "detail": "OK"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: Ошибка при входе - {str(e)}")