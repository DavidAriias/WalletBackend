from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AuditLog:
    id: Optional[int]
    user_id: int
    action: str
    entity: str
    entity_id: Optional[int]
    created_at: Optional[datetime] = None