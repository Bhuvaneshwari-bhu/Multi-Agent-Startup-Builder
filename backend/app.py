from fastapi import FastAPI
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
app = FastAPI(
    title="AI Startup Builder API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-project.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)