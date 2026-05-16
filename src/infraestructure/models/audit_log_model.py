from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.infraestructure.db.base import Base

class AuditLogModel(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    action = Column(String, nullable=False)
    entity = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)