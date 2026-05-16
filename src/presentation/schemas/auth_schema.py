from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=100)

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: int