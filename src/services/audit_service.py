from src.domain.entities.audit_log import AuditLog

class AuditService:

    def __init__(self, audit_repo):
        self.audit_repo = audit_repo

    def log(
        self,
        user_id: int,
        action: str,
        entity: str,
        entity_id: int = None
    ):
        log = AuditLog(
            id=None,
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
            created_at=None
        )

        self.audit_repo.create(log)

    def list_logs(self, limit: int = 100):

        logs = self.audit_repo.get_all(limit)

        return [
            AuditLog(
                id=l.id,
                user_id=l.user_id,
                action=l.action,
                entity=l.entity,
                entity_id=l.entity_id,
                created_at=l.created_at
            )
            for l in logs
        ]