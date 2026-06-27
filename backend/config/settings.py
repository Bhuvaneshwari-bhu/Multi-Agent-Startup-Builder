# config/settings.py

# Gemini Models (priority order)
GEMINI_MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
]

# Retry Configuration
MAX_RETRIES = 2
RETRY_DELAY = 2  # seconds

# Agent Limits
MAX_AGENT_WORDS = 60

# PDF
PDF_OUTPUT_PATH = "reports/startup_report.pdf"

# Application
APP_NAME = "AI Startup Builder"
APP_VERSION = "1.0.0"