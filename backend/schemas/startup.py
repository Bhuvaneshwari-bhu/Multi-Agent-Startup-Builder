from pydantic import BaseModel


class StartupRequest(BaseModel):
    startup_idea: str