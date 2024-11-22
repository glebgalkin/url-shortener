from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class URLRequest(BaseModel):
    original_url: str

@router.post("/shorten", tags=["shorten"])
async def shorten_url(request: URLRequest):
    print(request)
    return 'Hello'