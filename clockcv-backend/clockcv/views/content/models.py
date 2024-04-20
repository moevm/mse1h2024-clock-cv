from enum import StrEnum
from pydantic import BaseModel


class PhotoUploadStatus(StrEnum):
    ok = "ok"
    file_not_image = "file not image"


class PhotoUploadResponse(BaseModel):
    imageId: str | None
    result: int | None
    description: str | None | PhotoUploadStatus


class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


class CreateUserStatus(StrEnum):
    ok = "ok"
    error = "error"
    user_already_exist = "user_already_exist"

class CreateUserResponse(BaseModel):
    userId: int | None
    status: CreateUserStatus = CreateUserStatus.ok


class CheckUserBody(BaseModel):
    email: str
    password: str


class CheckUserStatus(StrEnum):
    ok = "ok"
    error = "error"
    no_user_with_this_email = "no_user_with_this_email"
    incorrect_password = "incorrect_password"


class CheckUserResponse(BaseModel):
    userId: int | None
    userName: str | None
    status: CheckUserStatus = CreateUserStatus.ok
