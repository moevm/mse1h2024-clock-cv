from enum import StrEnum
from pydantic import BaseModel


class PhotoUploadStatus(StrEnum):
    ok = "ok"
    file_not_image = "file not image"


class PhotoUploadResponse(BaseModel):
    imageId: str | None
    result: int | None
    description: str | None | PhotoUploadStatus
