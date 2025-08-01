# app/main.py
import spacy
from datetime import timedelta
from typing import List 
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError

from . import models, crud, logic, security, config
from . import pydantic_models as schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Analyzer API")
nlp = spacy.load("en_core_web_sm")

# --- CORS Middleware (no changes) ---
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dependency for DB session (no changes) ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- New Authentication Dependency ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

# --- API Endpoints ---
@app.post("/users/", response_model=schemas.User)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # ... (same as before)
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # ... (same as before)
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/analyses/", response_model=List[schemas.AnalysisResponse])
def read_user_analyses(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    analyses = crud.get_analyses_by_user(db, user_id=current_user.id)
    return analyses

# --- MODIFIED /analyze-skills/ ENDPOINT ---
@app.post("/analyze-skills/", response_model=schemas.AnalysisResponse)
def analyze_resume_skills(
    request: schemas.ResumeRequest, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    detected_skills = logic.extract_skills(request.resume_text, nlp)
    db_analysis = models.Analysis(
        analysis_type="skills",
        results={"detected_skills": detected_skills},
        owner_id=current_user.id  # Link the analysis to the logged-in user
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis