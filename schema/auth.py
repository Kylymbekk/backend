from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, validator, Field


class StatusEnum(str, Enum):
    admin = 'admin'
    client = 'client',
    manager = 'manager'


class RegisterPostIn(BaseModel):
    name: Optional[str] = 'asan'
    surname: str = Field(min_length=2, max_length=20)
    email: EmailStr
    password: str
    # password1: str
    status: StatusEnum

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    # @validator('password')
    # def passwords_match(cls, v, values, **kwargs):
    #     if 'password1' in values and v != values['password1']:
    #         raise ValueError('passwords do not match')
    #     return v


class LoginPostIn(BaseModel):
    email: EmailStr
    password: str




