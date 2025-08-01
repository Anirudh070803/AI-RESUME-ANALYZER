# app/pydantic_models.py
from pydantic import BaseModel, ConfigDict
from typing import Any

class ResumeRequest(BaseModel):
    resume_text: str

class CompareRequest(BaseModel):
    resume_text: str
    jd_text: str

# Add this new model for the response
class AnalysisResponse(BaseModel):
    id: int
    analysis_type: str
    results: Any

    # This tells Pydantic to work with SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)