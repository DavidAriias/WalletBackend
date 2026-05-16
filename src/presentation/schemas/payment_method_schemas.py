from pydantic import BaseModel, Field
from typing import Optional, Literal


class PaymentMethodCreate(BaseModel):
    type: Literal[
        "card",
        "bank_account",
        "clabe"
    ]

    alias: str = Field(
        ...,
        max_length=50
    )

    institution: str = Field(
        ...,
        max_length=100
    )

    currency: str = Field(
        ...,
        min_length=3,
        max_length=3
    )

    identifier: str = Field(
        ...,
        max_length=255
    )


class PaymentMethodUpdate(BaseModel):
    alias: Optional[str] = Field(
        None,
        max_length=50
    )

    institution: Optional[str] = Field(
        None,
        max_length=100
    )

    currency: Optional[str] = Field(
        None,
        min_length=3,
        max_length=3
    )

    is_active: Optional[bool] = True


class PaymentMethodResponse(BaseModel):
    id: int
    type: str
    alias: str
    institution: str
    currency: str
    is_active: bool
    masked_identifier: str

class PaymentMethodListResponse(BaseModel):
    items: list[PaymentMethodResponse]
    total: int
    page: int
    page_size: int