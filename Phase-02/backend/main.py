"""
FastAPI Backend - Main Application Entry Point

This module initializes and configures the FastAPI application for the
Public Todo MVP. It sets up CORS, logging, database tables, and API routes.

Features:
- RESTful API for todo operations
- CORS configuration for frontend integration
- Automatic database table creation on startup
- Structured logging
- Lifespan events for startup/shutdown tasks

Tech Stack:
- FastAPI: Modern web framework for building APIs
- SQLModel: SQL database ORM with Pydantic integration
- Neon Postgres: Cloud-hosted PostgreSQL database

Author: Shayan
Project: SDD-Hackathon-02 Phase-02
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.todos import router as todos_router
from logging_config import setup_logging
from database.engine import engine
from sqlmodel import SQLModel
from models.todo import TodoItem
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    
    Handles startup and shutdown events:
    - Startup: Creates all database tables if they don't exist
    - Shutdown: Performs cleanup operations (if needed)
    
    Args:
        app (FastAPI): The FastAPI application instance
        
    Yields:
        None: Control back to the application during its lifetime
    """
    # Startup: Create database tables
    SQLModel.metadata.create_all(bind=engine)
    yield
    # Shutdown: cleanup if needed

# Initialize FastAPI application with lifespan management
app = FastAPI(lifespan=lifespan)

# Set up logging configuration
setup_logging(app)

# CORS (Cross-Origin Resource Sharing) configuration
# Allows frontend applications to make requests to this API
import os

# Get CORS origins from environment variable or use defaults
cors_origins_env = os.getenv("CORS_ORIGINS", "")
if cors_origins_env:
    origins = [origin.strip() for origin in cors_origins_env.split(",")]
else:
    origins = [
        "http://localhost:3000",      # Next.js default dev server
        "http://127.0.0.1:3000",  
        "https://sdd-hackathon-02-p1.vercel.app"    # Alternative localhost
    ]

# Add CORS middleware to allow cross-origin requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # List of allowed origins
    allow_credentials=True,          # Allow cookies and authentication
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all headers
)

# Include the todos API router with /api prefix
# All todo endpoints will be available under /api/todos
app.include_router(todos_router, prefix="/api")