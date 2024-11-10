from pydantic import BaseModel
from datetime import date

class SubscriptionNotificationResponse(BaseModel):
    logo: str
    days_until_due: int
    notification_date: date
    service_name: str
