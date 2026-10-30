from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    id: Optional[int] = None
    name: str
    course : str
    marks : float



# add 0 to 100 condition
