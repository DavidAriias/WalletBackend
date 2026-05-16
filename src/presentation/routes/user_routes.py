from fastapi import APIRouter, Depends
from src.services.user_service import UserService
from src.config.di.dependencies_injection import get_user_service
from src.config.security import get_current_user


router = APIRouter(prefix="/users", tags=["Users"])



@router.get("/me")
def get_profile(
    current_user=Depends(get_current_user),
    service: UserService = Depends(get_user_service)
):
    return service.get_profile(user_id= current_user.id)