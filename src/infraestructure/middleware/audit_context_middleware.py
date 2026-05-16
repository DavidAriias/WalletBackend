from starlette.middleware.base import BaseHTTPMiddleware
from src.helpers.jwt_helper import JWTHelper
from src.config.context.user_context import current_user_id


class AuthContextMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        auth = request.headers.get("Authorization")

        if auth:
            token = auth.replace("Bearer ", "")
            payload = JWTHelper.decode_token(token)
            user_id = JWTHelper.get_user_id(payload)


            current_user_id.set(user_id)

        response = await call_next(request)
        return response