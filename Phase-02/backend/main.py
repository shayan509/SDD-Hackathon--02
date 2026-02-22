from contextlib import asynccontextmanager
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from api.v1.endpoints.auth import router as auth_router
from api.v1.endpoints.todos import router as todos_router
from database.engine import engine
from logging_config import setup_logging

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    reset_on_start = os.getenv("RESET_DB_ON_START", "").lower() in {"1", "true", "yes"}
    if reset_on_start:
        SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
setup_logging(app)

cors_origins_env = os.getenv("CORS_ORIGINS", "")
if cors_origins_env:
    origins = [origin.strip() for origin in cors_origins_env.split(",") if origin.strip()]
else:
    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://sdd-hackathon-02-p1.vercel.app"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(todos_router, prefix="/api")
