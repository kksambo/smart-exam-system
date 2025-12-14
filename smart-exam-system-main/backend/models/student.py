

from sqlalchemy import Column, Integer, String
from backend.database import Base


class Student(Base):
   

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_names = Column(String(100), nullable=False)
    stud_nr = Column(String(9), nullable=False)
    cell_num = Column(String(10), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(50), nullable=False)
    faculty = Column(String(100), nullable=False)
