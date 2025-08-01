from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    analysis_type = Column(String, index=True)
    results = Column(JSON)
    # Add the foreign key to link to the users table
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Create the relationship
    owner = relationship("User", back_populates="analyses")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Create the reverse relationship
    analyses = relationship("Analysis", back_populates="owner")