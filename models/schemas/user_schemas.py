from typing import Annotated, Optional

from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    number: str = Field(..., pattern=r'^\+?\d{10,15}$', example='+1234567890')
    password: str = Field(..., min_length=6, example='yourpassword')
    fullname: str = Field(..., example='John Doe')
    acc_status: str = Field(..., example='active')  # Активен или заблокирован
    user_status: str = Field(..., example='regular')  # Статус пользователя
    is_moderator: Optional[bool] = Field(False, example=False)  # По умолчанию не модератор

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    number: str = Field(..., pattern=r'^\+?\d{10,15}$', example='+1234567890')
    fullname: str = Field(..., example='John Doe')
    acc_status: str = Field(..., example='active')  # Активен или заблокирован
    user_status: str = Field(..., example='regular')  # Статус пользователя
    is_moderator: Optional[bool] = Field(False, example=False)  # По умолчанию не модератор

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    number: str = Field(..., pattern=r'^\+?\d{10,15}$', example='+1234567890')
    password: str = Field(..., min_length=6, example='yourpassword')

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"