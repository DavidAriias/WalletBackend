from fastapi import Depends

from src.infraestructure.db.dependencies import get_db

# Repositories
from src.infraestructure.repositories.user_repository import (
    UserRepository
)
from src.infraestructure.repositories.payment_method_repository import (
    PaymentMethodRepository
)
from src.infraestructure.repositories.audit_log_repository import AuditLogRepository

# Services
from src.services.auth_service import (
    AuthService
)
from src.services.user_service import (
    UserService
)
from src.services.payment_method_service import (
    PaymentMethodService
)
from src.services.audit_service import AuditService



# -------------------------
# Repositories
# -------------------------

def get_user_repository(
    db=Depends(get_db)
):
    return UserRepository(db)


def get_payment_method_repository(
    db=Depends(get_db)
):
    return PaymentMethodRepository(db)


# -------------------------
# Services
# -------------------------

def get_auth_service(
    repo=Depends(get_user_repository)
):
    return AuthService(repo)


def get_user_service(
    repo=Depends(get_user_repository)
):
    return UserService(repo)


def get_payment_method_service(
    repo=Depends(
        get_payment_method_repository
    )
):
    return PaymentMethodService(repo)

def get_audit_repository(db=Depends(get_db)):
    return AuditLogRepository(db)


def get_audit_service(repo=Depends(get_audit_repository)):
    return AuditService(repo)