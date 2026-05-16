from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AuditLogResponse(BaseModel):
    id: int
    user_id: int
    action: str
    entity: str
    entity_id: Optional[int] = None
    created_at: datetime