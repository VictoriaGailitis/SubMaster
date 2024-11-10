from fastapi import APIRouter, HTTPException, Depends
from peewee import DoesNotExist
from responses.user import UserResponse
from models.user import User
from payloads.user import UpdateUserPayload, UpdatePasswordPayload, BindCardPayload
from cryptography.fernet import Fernet
import os

CRYPTO_KEY = os.getenv("CRYPTO_KEY", Fernet.generate_key())
FERNET = Fernet(CRYPTO_KEY)

user_router = APIRouter(prefix='/user', tags=['Пользователь'])

@user_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    try:
        user = User.get(User.id == user_id)
        return UserResponse.from_orm(user)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Пользователь не найден")


@user_router.patch("/{user_id}/name", response_model=UserResponse)
def update_user_name(user_id: int, payload: UpdateUserPayload):
    try:
        user = User.get(User.id == user_id)
        user.name = payload.name
        user.save()
        return UserResponse.from_orm(user)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Пользователь не найден")


@user_router.patch("/{user_id}/password", response_model=UserResponse)
def update_user_password(user_id: int, payload: UpdatePasswordPayload):
    try:
        user = User.get(User.id == user_id)

        if FERNET.decrypt(user.password) != FERNET.decrypt(payload.old_password):
            raise HTTPException(status_code=400, detail="Неверный старый пароль")

        user.password = FERNET.encrypt(payload.new_password.encode()).decode()
        user.save()
        return UserResponse.from_orm(user)

    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Пользователь не найден")


@user_router.patch("/{user_id}/bind-card", response_model=UserResponse)
def bind_card(user_id: int, payload: BindCardPayload):
    try:
        user = User.get(User.id == user_id)

        user.card_number = payload.card_number
        user.save()

        return UserResponse.from_orm(user)

    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Пользователь не найден")