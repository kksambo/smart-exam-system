"""
Subject Pydantic schemas.
"""

from pydantic import BaseModel


class SubjectBase(BaseModel):
   

    subject_name: str
    subject_code: str


class SubjectRead(SubjectBase):
  

    id: int

    class Config:
        from_attributes = True
