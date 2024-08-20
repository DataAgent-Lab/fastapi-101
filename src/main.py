from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_v1.api import router as api_router


title = "My API"
app = FastAPI(
    title=f"{title}",
    service_name="my_api",
    description="Server-Side Event for My API",
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
async def root():
    return {"message": f"{title} API is ready!"}

@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
