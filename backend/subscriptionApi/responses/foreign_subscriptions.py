from pydantic import BaseModel
from typing import List
from datetime import date

class ForeignSubscriptionResponse(BaseModel):
    id: int
    name: str
    logo: str
    description: str
    plans: List[int]
    periodities: List[int]

class UserForeignSubscriptionResponse(BaseModel):
    id: int
    subscription: ForeignSubscriptionResponse
    plan: int
    periodity: int
    price: float
    start_date: date
    expiration_date: date
    activation_code: str

class AvailableForeignSubscriptionResponse(BaseModel):
    id: int
    name: str
    logo: str
    min_price: float

class OneForeignSubscriptionPurchaseResponse(BaseModel):
    id: int
    name: str
    logo: str
    description: str
    plans: List[int]
    periodities: List[int]
    auto_renewal_available: bool
