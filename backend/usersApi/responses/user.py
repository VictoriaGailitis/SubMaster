from pydantic import BaseModel, EmailStr, Field

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    card_number: str = None

    class Config:
        orm_mode = True
