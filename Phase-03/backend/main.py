"""
FastAPI Backend - Main Application Entry Point

This module initializes and configures the FastAPI application for the
Public Todo MVP (Enhanced Version). It sets up CORS, logging, database 
tables, and API routes with improved architecture and error handling.

Features:
- RESTful API for todo operations (CRUD)
- CORS configuration for frontend integration
- Automatic database table creation on startup
- Structured logging with custom configuration
- Lifespan events for startup/shutdown tasks
- Enhanced error handling and validation

Tech Stack:
- FastAPI: Modern, fast web framework for building APIs
- SQLModel: SQL database ORM with Pydantic integration
- Neon Postgres: Cloud-hosted PostgreSQL database with SSL
- Docker: Containerization support

Author: Shayan
Project: SDD-Hackathon-02 Phase-03
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.endpoints.todos import router as todos_router
from logging_config import setup_logging
from database.engine import engine
from sqlmodel import SQLModel
from models.todo import TodoItem

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    
    Manages the application lifecycle with proper startup and shutdown handling:
    - Startup: Initializes database tables using SQLModel metadata
    - Shutdown: Performs cleanup operations (connection pooling, etc.)
    
    This ensures resources are properly managed throughout the application's lifetime.
    
    Args:
        app (FastAPI): The FastAPI application instance
        
    Yields:
        None: Control back to the application during its runtime
    """
    # Startup: Create database tables if they don't exist
    SQLModel.metadata.create_all(bind=engine)
    yield
    # Shutdown: cleanup if needed (connection pools, background tasks, etc.)

# Initialize FastAPI application with lifespan management
app = FastAPI(lifespan=lifespan)

# Set up structured logging configuration
setup_logging(app)

# CORS (Cross-Origin Resource Sharing) configuration
# Defines which frontend origins are allowed to make requests to this API
origins = [
    "http://localhost:3000",      # Next.js default development server
    "http://127.0.0.1:3000",      # Alternative localhost notation
    "http://localhost:5173",      # Vite default development server
    "http://127.0.0.1:5173",      # Alternative localhost notation
]

# Add CORS middleware to enable cross-origin requests
# This is essential for frontend-backend communication in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Whitelist of allowed origins
    allow_credentials=True,          # Allow cookies and authentication headers
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, PATCH, DELETE)
    allow_headers=["*"],             # Allow all request headers
)

# Include the todos API router with /api prefix
# All todo-related endpoints will be accessible under /api/todos
app.include_router(todos_router, prefix="/api")