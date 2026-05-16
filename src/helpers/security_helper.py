from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from src.config import settings


class SecurityHelper:
    _pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    )

    @classmethod
    def hash_password(cls, password: str) -> str:
        return cls._pwd_context.hash(password)

    @classmethod
    def verify_password(
        cls,
        plain_password: str,
        hashed_password: str
    ) -> bool:
        return cls._pwd_context.verify(
            plain_password,
            hashed_password
        )

    @classmethod
    def create_access_token(
        cls,
        data: dict
    ) -> str:
        payload = data.copy()

        expire = datetime.utcnow() + timedelta(
            minutes=settings.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload.update({
            "exp": expire
        })

        return jwt.encode(
            payload,
            settings.settings.SECRET_KEY,
            algorithm= settings.settings.ALGORITHM
        )
    
    @classmethod
    def hash_identifier(
        cls,
        identifier: str
    ) -> str:
        return cls._pwd_context.hash(identifier)