# app/pydantic_models.py
from pydantic import BaseModel, ConfigDict
from typing import Any, Optional

class ResumeRequest(BaseModel):
    resume_text: str

class CompareRequest(BaseModel):
    resume_text: str
    jd_text: str
    
class AnalysisResponse(BaseModel):
    id: int
    analysis_type: str
    results: Any
    model_config = ConfigDict(from_attributes=True)
    
#Add these new User Schemas
class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: Optional[str] = None