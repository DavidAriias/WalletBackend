
from src.presentation.schemas.user_schema import UserResponse

class UserService:
     
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_profile(self, user_id: int):
        user = self.user_repo.get_by_id(user_id)
        return UserResponse(
            id= user.id,
            email= user.email,
            is_active= user.is_active,
        )