

from sqlalchemy import Column, Integer, ForeignKey
from backend.database import Base


class StudentSubject(Base):
 

    __tablename__ = "student_subjects"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
