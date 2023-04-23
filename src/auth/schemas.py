from enum import Enum
from typing import NamedTuple

from pydantic import BaseModel, Field, validator, ValidationError


class User(BaseModel):

    name: str = Field(max_length=30)
    email: str = Field(max_length=50)
    password: str = Field(max_length=100)

    @validator("name")
    @classmethod
    def validation_name(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError("Value name for user not validate!")

        return value

    @validator("email")
    @classmethod
    def validation_email(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError("Value name for email not validate!")

        if not "@" in value:
            raise ValueError("Value email for user not validate!")

        return value


class AuthUser(BaseModel):

    email: str = Field(max_length=30)
    password: str = Field(max_length=50)

    @validator("email")
    @classmethod
    def validation_email(cls, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Value name for email not validate!")

        if not "@" in value:
            raise ValueError("Value email for user not validate!")

        return value


class Status(Enum):

    true = "success"
    false = "not success"


class AddableUser(BaseModel):

    name: str = Field(max_length=30)
    email: str = Field(max_length=50)

    @validator("name")
    @classmethod
    def validation_name(cls, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Value name for user not validate!")

        return value

    @validator("email")
    @classmethod
    def validation_email(cls, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Value name for email not validate!")

        if not "@" in value:
            raise ValueError("Value email for user not validate!")

        return value


class ResponseForAuth(BaseModel):

    status: Status
    state: str = Field(max_length=50)


class ResponseForReg(BaseModel):

    status: Status
    addable_user: AddableUser | str


class UserHashedPassword(NamedTuple):

    name: str
    email: str
    hashed_password: str


class ResponseGetUser(NamedTuple):

    id: int
    name: str
    email: str
    hashed_password: str
    date_registration: str