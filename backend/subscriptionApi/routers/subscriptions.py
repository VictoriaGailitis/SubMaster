from datetime import date, timedelta, datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from responses.russian_subscriptions import UserRussianSubscriptionResponse
from models.subscription import UserRussianSubscriptions, ForeignSubscriptions, RussianSubscriptions, UserForeignSubscription
from responses.notifications import SubscriptionNotificationResponse
from responses.foreign_subscriptions import UserForeignSubscriptionResponse, AvailableForeignSubscriptionResponse, OneForeignSubscriptionPurchaseResponse
from payloads.subscription_purchase import SubscriptionCreationRequest

subscription_router = APIRouter(prefix='/subscriptions', tags=['Подписки'])


@subscription_router.get("/", response_model=List[UserRussianSubscriptionResponse])
def get_user_subscriptions(user_id: int, country_filter: Optional[str] = None, page: int = Query(1, ge=1),
                           limit: int = Query(10, ge=1)):
    query = UserRussianSubscriptions.select().where(UserRussianSubscriptions.user_id == user_id)

    if country_filter == "foreign":
        query = query.join(ForeignSubscriptions).where(ForeignSubscriptions.id == UserRussianSubscriptions.subscription)

    elif country_filter == "russian":
        query = query.join(RussianSubscriptions).where(RussianSubscriptions.id == UserRussianSubscriptions.subscription)

    subscriptions = query.paginate(page, limit)

    return [UserRussianSubscriptionResponse.from_orm(sub) for sub in subscriptions]


@subscription_router.get("/notifications", response_model=List[SubscriptionNotificationResponse])
def get_subscription_notifications(user_id: int):
    notifications = []

    user_subscriptions = UserForeignSubscription.select().where(UserForeignSubscription.user_id == user_id)

    for subscription in user_subscriptions:
        days_until_due = (subscription.expiration_date - date.today()).days

        if days_until_due <= 3:
            notifications.append(SubscriptionNotificationResponse(
                logo=subscription.subscription.logo,
                days_until_due=days_until_due,
                notification_date=date.today(),
                service_name=subscription.subscription.name
            ))

    return notifications


@subscription_router.get("/foreign/{subscription_id}", response_model=UserForeignSubscriptionResponse)
def get_user_foreign_subscription(user_id: int, subscription_id: int):
    try:
        subscription = UserForeignSubscription.get(UserForeignSubscription.id == subscription_id)
        return UserForeignSubscriptionResponse.from_orm(subscription)
    except:
        raise HTTPException(status_code=404, detail="Подписка не найдена")


@subscription_router.patch("/foreign/{subscription_id}/auto-renewal", response_model=UserForeignSubscriptionResponse)
def toggle_auto_renewal(subscription_id: int):
    try:
        subscription = UserForeignSubscription.get(UserForeignSubscription.id == subscription_id)

        subscription.auto_renewal = not subscription.auto_renewal
        subscription.save()

        return UserForeignSubscriptionResponse.from_orm(subscription)

    except UserForeignSubscription.DoesNotExist:
        raise HTTPException(status_code=404, detail="Подписка не найдена")


@subscription_router.get("/russian/{subscription_id}", response_model=UserRussianSubscriptionResponse)
def get_user_russian_subscription(subscription_id: int):
    try:
        subscription = UserRussianSubscriptions.get(UserRussianSubscriptions.id == subscription_id)
        return UserRussianSubscriptionResponse.from_orm(subscription)

    except UserRussianSubscriptions.DoesNotExist:
        raise HTTPException(status_code=404, detail="Подписка не найдена")


@subscription_router.get("/foreign/available", response_model=List[AvailableForeignSubscriptionResponse])
def get_available_foreign_subscriptions():
    subscriptions = ForeignSubscriptions.select()
    return [AvailableForeignSubscriptionResponse(id=sub.id, name=sub.name, logo=sub.logo, min_price=min(sub.plans)) for
            sub in subscriptions]


@subscription_router.get("/foreign/purchase/{subscription_id}", response_model=OneForeignSubscriptionPurchaseResponse)
def get_one_foreign_subscription_for_purchase(subscription_id: int):
    try:
        subscription = ForeignSubscriptions.get(ForeignSubscriptions.id == subscription_id)
        return OneForeignSubscriptionPurchaseResponse(
            id=subscription.id,
            name=subscription.name,
            logo=subscription.logo,
            description=subscription.description,
            plans=subscription.plans,
            periodities=subscription.periodities,
            auto_renewal_available=True
        )

    except ForeignSubscriptions.DoesNotExist:
        raise HTTPException(status_code=404, detail="Подписка не найдена")


@subscription_router.post("/foreign/purchase", response_model=UserForeignSubscriptionResponse)
def create_user_foreign_subscription(request_data: SubscriptionCreationRequest):

    try:
        foreign_subscription = ForeignSubscriptions.get(ForeignSubscriptions.id == request_data.subscription_id)

        new_subscription = UserForeignSubscription.create(
            subscription=foreign_subscription,
            plan=request_data.plan,
            periodity=request_data.periodity,
            price=request_data.price,
            start_date=date.today(),
            expiration_date=date.today() + timedelta(days=request_data.periodity * 30),
            activation_code="ACTIVATION_CODE_EXAMPLE",
            auto_renewal=request_data.auto_renewal,
            created_at=datetime.now(timezone.utc)
        )

        return UserForeignSubscriptionResponse.from_orm(new_subscription)

    except ForeignSubscriptions.DoesNotExist:
        raise HTTPException(status_code=404, detail="Зарубежная подписка не найдена")