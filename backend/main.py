"""
Smart Exam System - FastAPI Backend
-----------------------------------

This module initializes the FastAPI application for the Smart Exam System.
It contains a simple index route for health checking and verification that
the backend server is running correctly.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import init_db
from routers.auth import router as auth_router
from routers.lecturer import router as lecturer_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield



app = FastAPI(
    title="Smart Exam System API",
    description="Backend for the Smart Exam System application.",
    version="1.0.0",
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    """
    Root endpoint for the backend API.

    Returns:
        dict: A simple message indicating that the backend is running.
    """
    return {"message": "Backend is running"}


# Include authentication routes
app.include_router(auth_router)
app.include_router(lecturer_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
