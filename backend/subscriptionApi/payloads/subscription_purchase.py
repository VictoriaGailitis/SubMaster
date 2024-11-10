from pydantic import BaseModel
from datetime import date

class SubscriptionCreationRequest(BaseModel):
    user_id: int