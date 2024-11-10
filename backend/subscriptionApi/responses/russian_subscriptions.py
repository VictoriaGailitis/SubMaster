from pydantic import BaseModel
from datetime import date

class RussianSubscriptionResponse(BaseModel):
    id: int
    name: str
    logo: str
    description: str
    provider_url: str
    price: int
    start_date: date
    expiration_date: date
    periodity: int

class UserRussianSubscriptionResponse(BaseModel):
    id: int
    subscription: RussianSubscriptionResponse
    price: int
    start_date: date
    expiration_date: date
    periodity: int