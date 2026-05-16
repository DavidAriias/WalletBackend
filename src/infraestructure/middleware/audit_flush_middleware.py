from src.config.audit.collector import AuditCollector
from src.config.context.user_context import current_user_id
from src.domain.entities.audit_log import AuditLog
from src.infraestructure.db.dependencies import SessionLocal
from src.infraestructure.repositories.audit_log_repository import AuditLogRepository


async def audit_flush_middleware(request, call_next):
    response = await call_next(request)

    events = AuditCollector.flush()
    user_id = current_user_id.get()

    if events:
        if not user_id:
            print("No user_id found, skipping audit persistence")
            return response

        db = SessionLocal()
        repo = AuditLogRepository(db)

        try:
            for e in events:
                audit = AuditLog(
                    id=None,
                    user_id=user_id,
                    action=e["action"],
                    entity=e["entity"],
                    entity_id=e["entity_id"]
                )

                repo.create(audit)
        finally:
            db.close()

    return response