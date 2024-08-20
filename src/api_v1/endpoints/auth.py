from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
import os

load_dotenv()
DEFAULT_API_KEY = os.getenv("DEFAULT_API_KEY")
default_auth_header = APIKeyHeader(name="Authorization", auto_error=False)


def check_authorization(request: Request):
    auth_token = request.headers.get("Authorization", "")
    if auth_token != f"Bearer {DEFAULT_API_KEY}":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True
