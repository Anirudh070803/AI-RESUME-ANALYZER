# models.py
from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    analysis_type = Column(String, index=True)
    results = Column(JSON)