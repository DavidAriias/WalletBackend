from fastapi import APIRouter, Depends
from src.config.di.dependencies_injection import get_audit_service
from src.services.audit_service import AuditService
from src.presentation.schemas.audit_schema import AuditLogResponse

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.get("/", response_model=list[AuditLogResponse])
def get_logs(
    limit: int = 100,
    service: AuditService = Depends(get_audit_service)
):
    return service.list_logs(limit)