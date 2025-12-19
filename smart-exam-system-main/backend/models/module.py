

from sqlalchemy import Column, Integer, String
from backend.database import Base


class Subject(Base):
   

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String(100), nullable=False)
    
