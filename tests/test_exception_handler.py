import pytest
import json
from app.core.exceptions import AppException
from app.core.handlers import app_exception_handler
from fastapi.responses import JSONResponse



@pytest.mark.asyncio
async def test_error_response_schema():
    error=AppException("Invalid",500)
    response= await app_exception_handler(exc=error)

    assert isinstance(response,JSONResponse)

@pytest.mark.asyncio
async def test_message_preserved():
    error=AppException("Invalid",500)
    response=await app_exception_handler(exc=error)

    body=json.loads(response.body)

    assert body["error"]=="Invalid"

@pytest.mark.asyncio
async def test_status_code():
    error=AppException("Invalid",500)
    response= await app_exception_handler(error)

    assert response.status_code==500

