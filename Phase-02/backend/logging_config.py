import logging
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"{request.method} {request.url}")
        response = await call_next(request)
        return response


def setup_logging(app: FastAPI):
    """Set up logging infrastructure for the application."""
    app.add_middleware(LoggingMiddleware)


def get_logger(name: str = __name__):
    """Get a logger instance with the specified name."""
    return logging.getLogger(name)