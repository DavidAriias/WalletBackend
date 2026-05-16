from src.helpers.security_helper import SecurityHelper
from fastapi import HTTPException

from src.infraestructure.models.user_model import UserModel
from src.presentation.schemas.user_schema import UserResponse
from src.presentation.schemas.auth_schema import LoginResponse

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register(self, dto):
        existing = self.user_repo.get_by_email(dto.email)

        if existing:
             raise HTTPException(
                status_code=400,
                detail="User already exists"
            )

        user = UserModel(
            email=dto.email,
            password_hash= SecurityHelper.hash_password(dto.password)
        )

        created_user = self.user_repo.create(user)
        
        return UserResponse(
            id= created_user.id,
            email= created_user.email,
            is_active= created_user.is_active
        )

    def login(self, dto):
        user = self.user_repo.get_by_email(dto.email)

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Invalid credentials"
            )
        if not SecurityHelper.verify_password(dto.password, user.password_hash):
              raise HTTPException(
                status_code=400,
                detail="Invalid credentials"
            )

        token = SecurityHelper.create_access_token({
            "sub": str(user.id)
        })

        return LoginResponse(
            access_token=token,
            user_id=user.id
        )