from pydantic import BaseModel, EmailStr, Field

class RegistrationPayload(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(..., min_length=8, description="Пароль пользователя (не менее 8 символов)")
    password_retry: str = Field(..., description="Повторите пароль для подтверждения")

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "some_password",
                "password_retry": "some_password"
            }
        }