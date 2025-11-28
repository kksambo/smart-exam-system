"""
Authentication router for Smart Exam System.
Provides user registration, login, and JWT token generation.
"""

import os
import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin, UserOut, Token
from utilities.hashing import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ---------------------------------------------------------------------
# JWT Config
# ---------------------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_PLEASE")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ---------------------------------------------------------------------
# Helper: Create JWT Token
# ---------------------------------------------------------------------
def create_access_token(data: dict):
    """
    Generates a signed JWT access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ---------------------------------------------------------------------
# Register User
# ---------------------------------------------------------------------
@router.post("/register", response_model=UserOut)
async def register_user(payload: UserCreate, session: AsyncSession = Depends(get_db)):
    """
    Registers a new user by saving username and hashed password.
    """
    # Check if username exists
    stmt = select(User).where(User.username == payload.username)
    result = await session.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Create user
    new_user = User(
        username=payload.username,
        password=hash_password(payload.password)
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


# ---------------------------------------------------------------------
# Login User
# ---------------------------------------------------------------------
@router.post("/login", response_model=Token)
async def login(payload: UserLogin, session: AsyncSession = Depends(get_db)):
    """
    Authenticates user and returns a JWT access token.
    """
    # Find user
    stmt = select(User).where(User.username == payload.username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        return {"message": "Invalid username"}

    # Verify password
    if not verify_password(payload.password, user.password):

        return{"message": "Invalid password"}



    # Create JWT
    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer","message":"login success"}
