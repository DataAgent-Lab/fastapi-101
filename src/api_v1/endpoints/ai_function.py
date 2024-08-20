from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from .models import Error404Model, TestResponseModel, TestRequestModel

router = APIRouter()


@router.post(
    "/test_ai_function",
    response_model=TestResponseModel,
    responses={200: {"model": TestResponseModel}, 404: {"model": Error404Model}}
)
async def test_ai_function(item: TestRequestModel):
    # reply = your_ai_function(item.message)
    reply = f"Your message: {item.message}"
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"reply": reply}
    )
