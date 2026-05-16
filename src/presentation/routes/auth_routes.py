from fastapi import APIRouter, Depends
from src.config.di.dependencies_injection import get_auth_service
from src.presentation.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    dto: RegisterRequest,
    service=Depends(get_auth_service)
):
    return service.register(dto)


@router.post("/login")
def login(
    dto: LoginRequest,
    service=Depends(get_auth_service)
):
    return service.login(dto)