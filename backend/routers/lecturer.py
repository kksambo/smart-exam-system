"""
Lecturer routes for Smart Exam System.

This module provides basic CRUD operations for lecturers.
These routes are NOT protected and can be accessed publicly , the  security it non functional requirementts we will implement it  later.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models.lecturer import Lecturer

router = APIRouter(
    prefix="/lecturers",
    tags=["Lecturers"]
)


# ---------------------------------------------------------------------
# GET: All Lecturers
# ---------------------------------------------------------------------
@router.get("/")
async def get_all_lecturers(session: AsyncSession = Depends(get_db)):
    stmt = select(Lecturer)
    result = await session.execute(stmt)
    lecturers = result.scalars().all()
    return lecturers


# ---------------------------------------------------------------------
# GET: Lecturer by ID
# ---------------------------------------------------------------------
@router.get("/{lecturer_id}")
async def get_lecturer_by_id(
    lecturer_id: int,
    session: AsyncSession = Depends(get_db)
):
    stmt = select(Lecturer).where(Lecturer.id == lecturer_id)
    result = await session.execute(stmt)
    lecturer = result.scalar_one_or_none()

    if not lecturer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecturer not found"
        )

    return lecturer


# ---------------------------------------------------------------------
# POST: Create Lecturer
# ---------------------------------------------------------------------
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_lecturer(
    payload: dict,
    session: AsyncSession = Depends(get_db)
):
    try:
        lecturer = Lecturer(**payload)
    except TypeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid lecturer data"
        )

    session.add(lecturer)
    await session.commit()
    await session.refresh(lecturer)

    return lecturer


# ---------------------------------------------------------------------
# PUT: Update Lecturer
# ---------------------------------------------------------------------
@router.put("/{lecturer_id}")
async def update_lecturer(
    lecturer_id: int,
    payload: dict,
    session: AsyncSession = Depends(get_db)
):
    stmt = select(Lecturer).where(Lecturer.id == lecturer_id)
    result = await session.execute(stmt)
    lecturer = result.scalar_one_or_none()

    if not lecturer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecturer not found"
        )

    for key, value in payload.items():
        if hasattr(lecturer, key):
            setattr(lecturer, key, value)

    await session.commit()
    await session.refresh(lecturer)

    return lecturer


# ---------------------------------------------------------------------
# DELETE: Lecturer
# ---------------------------------------------------------------------
@router.delete("/{lecturer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lecturer(
    lecturer_id: int,
    session: AsyncSession = Depends(get_db)
):
    stmt = select(Lecturer).where(Lecturer.id == lecturer_id)
    result = await session.execute(stmt)
    lecturer = result.scalar_one_or_none()

    if not lecturer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecturer not found"
        )

    await session.delete(lecturer)
    await session.commit()
