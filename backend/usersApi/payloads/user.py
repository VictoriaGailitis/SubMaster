from pydantic import BaseModel, EmailStr, Field

class UpdateUserPayload(BaseModel):
    name: str = Field(..., max_length=255)


class UpdatePasswordPayload(BaseModel):
    old_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)


class BindCardPayload(BaseModel):
    card_number: str = Field(..., max_length=16)