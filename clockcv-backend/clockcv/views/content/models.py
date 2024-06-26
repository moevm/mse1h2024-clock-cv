from enum import StrEnum
from pydantic import BaseModel
from clockcv.repository.user import UserTest


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


class HistoryStatus(StrEnum):
    ok = "ok"
    user_not_found = "user_not_found"


class HistoryResponse(BaseModel):
    data: list
    status: HistoryStatus = HistoryStatus.ok


class RecoverPasswordStatus(StrEnum):
    ok = "ok"
    email_not_found = "email_not_found"
    sending_error = "sending_error"


class RecoverPasswordResponse(BaseModel):
    status: RecoverPasswordStatus = RecoverPasswordStatus.ok
