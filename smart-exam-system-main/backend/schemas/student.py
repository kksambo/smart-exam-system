

from pydantic import BaseModel


 

   


class StudentCreate(BaseModel):
     
    full_names: str
    stud_nr: str
    cell_num: str
    email : str
    password: str


class StudentRead(StudentBase):
  

    id: int

    class Config:
     

        from_attributes = True
