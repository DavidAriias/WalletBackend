from src.infraestructure.models.audit_log_model import AuditLogModel
from src.domain.entities.audit_log import AuditLog
from datetime import datetime


class AuditLogRepository:

    def __init__(self, db):
        self.db = db

    def create(self, entity: AuditLog):
        model = AuditLogModel(
            user_id=entity.user_id,
            action=entity.action,
            entity=entity.entity,
            entity_id=entity.entity_id,
            created_at=datetime.utcnow()
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return model
    
    def get_all(self, limit: int = 100):
        return (
            self.db.query(AuditLogModel)
            .order_by(AuditLogModel.created_at.desc())
            .limit(limit)
            .all()
        )