from pydantic import BaseModel
from typing import Optional

# Create user Base Model
class UserIn(BaseModel):
    name : str
    phoneno : str

class UserOut(BaseModel):
    id : int
    name : str
    phoneno : str

    class Config:
        orm_mode = True