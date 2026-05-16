from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentMethod:
    id: Optional[int]
    user_id: int
    type: str
    alias: str
    institution: str
    currency: str
    identifier_hash: str
    identifier_last4: str
    is_active: bool = True