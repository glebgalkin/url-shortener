from fastapi import FastAPI
from routers import url
from starlette.responses import RedirectResponse


app = FastAPI()

# Register each router manually
app.include_router(url.router, prefix="/api/v1")

@app.get("/redirect", tags=["shorten"])
async def redirect():
    original_url = 'https://www.youtube.com'
    return RedirectResponse(url=original_url, status_code=301)

