from enum import StrEnum
from pydantic import BaseModel

class TestBody(BaseModel):
    test_txt: str

class TestStatus(StrEnum):
    ok = "ok",
    error = "error"

class TestResponse(BaseModel):
    status:TestStatus
    content: str