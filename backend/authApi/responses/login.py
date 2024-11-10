from pydantic import BaseModel, Field

class Login(BaseModel):
    status: int = Field(default=200)
    description: str = Field(default="OK")
