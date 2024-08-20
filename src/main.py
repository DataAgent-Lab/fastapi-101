from fastapi import FastAPI, Request, Security
from fastapi.middleware.cors import CORSMiddleware

from api_v1.api import router as api_router
from api_v1.endpoints.auth import check_authorization, default_auth_header


title = "My API"
app = FastAPI(
    title=f"{title}",
    service_name="my_api",
    description="My AI Functions",
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS
    allow_headers=["*"],
)


@app.get("/")
async def root(request: Request, token = Security(default_auth_header)):
    assert check_authorization(request)

    return {"message": f"{title} API is ready!"}

@app.get("/health")
async def health(request: Request, token = Security(default_auth_header)):
    assert check_authorization(request)

    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
