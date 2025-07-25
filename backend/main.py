import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine, Base
from routers import users, permits

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Government Permit Management System", docs_url="/api/docs", openapi_url="/api/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(permits.router, prefix="/api/permits", tags=["Permits"])

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.exception_handler(Exception)
def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": f"Oops! Something went wrong: {exc}"})

if os.path.exists("static"):
    app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

    @app.get("/{file_path:path}")
    async def serve_frontend(file_path: str):
        if file_path.startswith("api/") or file_path.startswith("static/") or file_path == "":
            return None
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
