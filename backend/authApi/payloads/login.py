from pydantic import BaseModel, EmailStr, Field


class LoginPayload(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(..., description="Пароль пользователя")

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "strong_password123"
            }
        }