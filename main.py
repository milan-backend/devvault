from fastapi import FastAPI
from database import engine,Base

from dotenv import load_dotenv
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

from routes.auth.signup import router as signup_router
from routes.auth.login import router as login_router
from routes.project import router as project_router
from routes.secret.secret import router as secret_router


app = FastAPI(title="DevVault")

app.include_router(signup_router)
app.include_router(login_router)
app.include_router(project_router)
app.include_router(secret_router)

@app.get("/")
def root():
    return {
        "service": "DevVault API",
        "status" : "running",
        "documentation": "/docs"
        }