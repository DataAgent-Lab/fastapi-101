from pydantic import BaseModel


class ErrorContent(BaseModel):
    message: str

class Error404Model(BaseModel):
    status_code: int = 404
    content: ErrorContent

class TestRequestModel(BaseModel):
    message: str = "hello"

class TestResponseModel(BaseModel):
    reply: str = "I'm fine, thank you."

