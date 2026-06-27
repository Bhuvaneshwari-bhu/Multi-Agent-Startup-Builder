from fastapi import APIRouter

from schemas.startup import StartupRequest
from supervisors.startup_supervisor import startup_supervisor
from fastapi.responses import FileResponse
router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to AI Startup Builder API!"
    }


@router.post("/analyze")
def analyze(request: StartupRequest):

    state = startup_supervisor(request.startup_idea)

    return state

@router.get("/download-pdf")
def download_pdf():

    return FileResponse(
        "reports/startup_report.pdf",
        media_type="application/pdf",
        filename="startup_report.pdf"
    )