from src.infraestructure.models.user_model import UserModel
from src.domain.entities.user import User



class UserRepository:

    def __init__(self, db_session):
        self.db = db_session

    def get_by_id(self, user_id: int) :
        return (
            self.db.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

    def get_by_email(self, email: str):
        return (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )

    def create(self, user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return User(
            id= user.id,
            email= user.email,
            is_active= user.is_active,
            created_at=user.created_at,
        ) 