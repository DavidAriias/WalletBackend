from fastapi import Depends, HTTPException
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)
from jose import JWTError, ExpiredSignatureError

from src.helpers.jwt_helper import JWTHelper
from src.config.di.dependencies_injection import (
    get_user_service
)

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    user_service=Depends(
        get_user_service
    )
):
    token = credentials.credentials

    try:
        payload = JWTHelper.decode_token(
            token
        )

        user_id = JWTHelper.get_user_id(
            payload
        )

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = user_service.get_profile(
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user