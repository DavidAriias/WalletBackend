from contextvars import ContextVar

current_user_id: ContextVar[int] = ContextVar("current_user_id", default=None)