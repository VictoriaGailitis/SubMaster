from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(default="Николай")
    email: str = Field(default="test@mail.ru")
    password: str = Field(default="test@mail.ru")