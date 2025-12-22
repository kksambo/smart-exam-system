from pydantic import BaseModel, EmailStr
from typing import Optional

class LecturerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    mobile_number: Optional[str] = None
    office_phone: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None


class LecturerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile_number: Optional[str] = None
    office_phone: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None


class LecturerOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    mobile_number: Optional[str]
    office_phone: Optional[str]
    department: Optional[str]
    title: Optional[str]

    class Config:
        from_attributes = True  # Pydantic v2
