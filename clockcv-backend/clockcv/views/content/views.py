import logging
import cv2
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .models import PhotoUploadResponse, PhotoUploadStatus, CreateUserBody, CreateUserResponse, CreateUserStatus, \
    CheckUserResponse, CheckUserStatus, CheckUserBody, HistoryResponse, HistoryStatus, RecoverPasswordResponse, \
    RecoverPasswordStatus
from clockcv.CV.main import cv_image_recognise
import uuid
from clockcv.state import app_state
from .helpers import generate_password_sha256



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

class RecoverPasswordBody(BaseModel):
    email: str

@router.post("/recover-password")
async def recover_password(body: RecoverPasswordBody):
    # Генерируем и выводим пароль
    password_sha256 = generate_password_sha256()
    user = await app_state.user_repo.update_user_password(email=body.email, password=password_sha256)

    html_code = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Reset</title>
        <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #ffffff;
        }}

        .container {{
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #eaeaea;
            border-radius: 8px;
            background-color: #80cbc4;
        }}
        
        .frame{{
            max-width: 300px;
            left: 20;
            margin: 50px auto;
            padding: 20px;
            border-radius: 8px;
            background-color: #009688;
        }}

        h1, h3 {{
            color: #FFFFFF;
        }}

        p {{
            color: #FFFFFF;
        }}


        </style>
    </head>
    <body>

    <div class="container">
        <h1>Восстановление пароля</h1>
        <h3>Мы получили запрос на изменение пароля от вашей учетной записи.</h3>
        <h3>Ваш новый пароль:</h3>
        <div class="frame">
            <p>{password_sha256}</p>
        </div>
    </div>

    </body>
    </html>
    '''

    if user:
        # text = f"Ваш новый пароль:{password_sha256}"
        text = html_code
        try:
            await app_state.mail_client.send_message(to=body.email,
                                                     subject="Восстановление пароля в сервисе Clock-cv",
                                                     text=text)
            return RecoverPasswordResponse()
        except:
            logger.error(f"Can't sanding in {body.email}")
            return RecoverPasswordResponse(status = RecoverPasswordStatus.sending_error)
        return RecoverPasswordResponse(status = RecoverPasswordStatus)
    else:
        return RecoverPasswordResponse(status=RecoverPasswordStatus.email_not_found)