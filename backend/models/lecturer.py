from sqlalchemy import Column, Integer, String
from database import Base

class Lecturer(Base):
    __tablename__ = "lecturers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

    mobile_number = Column(String(20), nullable=True)
    office_phone = Column(String(20), nullable=True)

    department = Column(String(100), nullable=True)
    title = Column(String(50), nullable=True)
