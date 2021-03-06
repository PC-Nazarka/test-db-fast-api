from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base schema for user."""
    name: str
    surname: str
    phone: str
    email: EmailStr
    passport_id: str
    passport_series: str


class UserCreate(UserBase):
    """Create schema for user."""
    pass


class User(UserBase):
    """Main schema for read user."""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
