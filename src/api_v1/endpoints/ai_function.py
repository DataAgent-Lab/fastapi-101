from fastapi import APIRouter, Request, Security, status
from fastapi.responses import JSONResponse

from .models import Error404Model, TestResponseModel, TestRequestModel
from .auth import check_authorization, default_auth_header

router = APIRouter()


@router.post(
    "/test_ai_function",
    response_model=TestResponseModel,
    responses={200: {"model": TestResponseModel}, 404: {"model": Error404Model}}
)
async def test_ai_function(request: Request, item: TestRequestModel, token = Security(default_auth_header)):
    assert check_authorization(request)

    # reply = your_ai_function(item.message)
    reply = f"Your message: {item.message}"
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"reply": reply}
    )
