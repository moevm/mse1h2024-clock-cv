import logging

from fastapi import APIRouter
from .models import TestBody, TestResponse, TestStatus

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/_internal_/test", response_model=TestResponse)
async def get_test(
        body: TestBody
):
    if body.test_txt == "Test":
        return TestResponse(status = TestStatus.ok, content = "Nice")
    else:
        return TestResponse(status=TestStatus.error, content="Enter Test")