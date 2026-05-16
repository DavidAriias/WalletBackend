from jose import jwt, JWTError
from fastapi import HTTPException

from src.config import settings


class JWTHelper:

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                settings.settings.SECRET_KEY,
                algorithms=[settings.settings.ALGORITHM]
            )
            return payload

        except JWTError:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    @staticmethod
    def get_user_id(payload: dict) -> int:
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token payload"
            )

        return int(user_id)