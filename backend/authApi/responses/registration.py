from pydantic import BaseModel, Field

class Registration(BaseModel):
    detail: str = Field(default="OK")
