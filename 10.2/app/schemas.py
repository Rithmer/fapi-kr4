from typing import Optional

from pydantic import BaseModel, EmailStr, conint, constr


class ValidationErrorResponse(BaseModel):
    error: str
    code: int
    details: list[dict]


class UserPayload(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = "Unknown"
