from fastapi import APIRouter, Depends, status, Query

from src.config.di.dependencies_injection import get_payment_method_service
from src.presentation.schemas.payment_method_schemas import (
    PaymentMethodCreate,
    PaymentMethodListResponse,
    PaymentMethodResponse
)
from src.config.security import get_current_user
from src.services.payment_method_service import (
    PaymentMethodService
)

router = APIRouter(
    prefix="/payment-methods",
    tags=["Payment Methods"]
)


@router.post(
    "/",
    response_model=PaymentMethodResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payment_method(
    payload: PaymentMethodCreate,
    current_user=Depends(get_current_user),
    service: PaymentMethodService = Depends(
        get_payment_method_service
    )
):
    return service.create(
        payload,
        current_user.id 
    )


@router.get(
    "/",
    response_model=PaymentMethodListResponse
)
def list_payment_methods(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    type: str | None = None,
    status: str | None = None,
    current_user=Depends(get_current_user),
    service: PaymentMethodService = Depends(
        get_payment_method_service
    )
):
    return service.list_by_user(
        user_id=current_user.id,
        page=page,
        page_size=page_size,
        type=type,
        status=status
    )


@router.get(
    "/{payment_method_id}",
    response_model=PaymentMethodResponse
)
def get_payment_method(
    payment_method_id: int,
    current_user=Depends(get_current_user),
    service: PaymentMethodService = Depends(
        get_payment_method_service
    )
):
    return service.get_detail(
        current_user.id,
        payment_method_id
    )


@router.delete(
    "/{payment_method_id}",
    response_model=PaymentMethodResponse
)
def delete_payment_method(
    payment_method_id: int,
    current_user=Depends(get_current_user),
    service: PaymentMethodService = Depends(
        get_payment_method_service
    )
):
    return service.deactivate(
        current_user.id,
        payment_method_id
    )