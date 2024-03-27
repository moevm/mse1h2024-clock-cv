import logging
import cv2
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from .models import PhotoUploadResponse, PhotoUploadStatus
from clockcv.CV.main import cv_image_recognise
import uuid

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/upload", response_model=PhotoUploadResponse)
async def photo_upload(file: UploadFile):
    if "image" not in file.content_type:
        logger.error(
            "Uploaded file is not image, mime_type=%s", file.content_type
        )
        return PhotoUploadResponse(
            imageId=None,
            result=None,
            description=PhotoUploadStatus.file_not_image
        )

    recognise_result = await cv_image_recognise(file=file)
    if (recognise_result[1]!=None):
        file_name = uuid.uuid4()
        full_file_name = f'storage/{file_name}.png'
        cv2.imwrite(filename=full_file_name, img=recognise_result[0])
    else:
        file_name = None
    return PhotoUploadResponse(imageId=str(file_name), result=recognise_result[1], description=recognise_result[2])


@router.get("/images", response_class=FileResponse)
async def get_photo(id: str):
    file = f"storage/{id}.png"
    return FileResponse(file)
