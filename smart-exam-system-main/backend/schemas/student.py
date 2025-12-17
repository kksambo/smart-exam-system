
from typing import List
from pydantic import BaseModel


class StudentBase(BaseModel):
  

    full_names: str
    stud_nr: str
    cell_num: str
    faculty: str


class StudentCreate(StudentBase):
 

    email: str
    password: str
    subject_ids: List[int]
