import logging
import cv2
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from .models import PhotoUploadResponse, PhotoUploadStatus, CreateUserBody, CreateUserResponse, CreateUserStatus, \
    CheckUserResponse, CheckUserStatus, CheckUserBody, HistoryResponse, HistoryStatus
from clockcv.CV.main import cv_image_recognise
import uuid
from clockcv.state import app_state

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/upload", response_model=PhotoUploadResponse)
async def photo_upload(file: UploadFile, user_id: int | None = None):
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
    if recognise_result[1] != None:
        file_name = uuid.uuid4()
        full_file_name = f'storage/{file_name}.png'
        cv2.imwrite(filename=full_file_name, img=recognise_result[0])

        logger.info(f"User_id: {user_id}")
        if user_id:
            # Тут прописатьсохранение результатов в бд -> в user_tests
            user_test = await app_state.user_repo.record_user_test(user_id=user_id,
                                                                   recognise_result=recognise_result[1],
                                                                   description=recognise_result[2])
            logger.info(user_test.description)
            logger.info(user_test.date)

    else:
        file_name = None

    return PhotoUploadResponse(imageId=str(file_name), result=recognise_result[1], description=recognise_result[2])


@router.get("/images", response_class=FileResponse)
async def get_photo(id: str):
    file = f"storage/{id}.png"
    return FileResponse(file)


@router.post("/create-user")
async def create_user(body: CreateUserBody):
    is_existed_user = await app_state.user_repo.get_user_by_email(email=body.email)
    if is_existed_user:
        return CreateUserResponse(userId=None, status=CreateUserStatus.user_already_exist)
    user = await app_state.user_repo.create_user(name=body.name, email=body.email, password=body.password)
    if user:
        return CreateUserResponse(userId=user.id)
    else:
        return CreateUserResponse(userId=None, status=CreateUserStatus.error)


@router.post("/entry-user")
async def entry_user(body: CheckUserBody):
    is_existed_user = await app_state.user_repo.get_user_by_email(email=body.email)
    if not is_existed_user:
        return CheckUserResponse(userId=None, userName=None, status=CheckUserStatus.no_user_with_this_email)
    else:
        password_is_correct = await app_state.user_repo.check_user_by_password(email=body.email, password=body.password)
        if not password_is_correct:
            return CheckUserResponse(userId=None, userName=None, status=CheckUserStatus.incorrect_password)
        else:
            return CheckUserResponse(userId=password_is_correct.id, userName=password_is_correct.name)


@router.get("/history")
async def history_user(id: int):
    user_history = await app_state.user_repo.get_user_history(user_id=id)
    if not user_history:
        return HistoryResponse(data=list(), status=HistoryStatus.user_not_found)
    return HistoryResponse(data=user_history)