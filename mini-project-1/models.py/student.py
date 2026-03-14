from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import List
from .enrollment import Enrollment

class Student(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    department: str = Field(min_length=2, max_length=100)
    enrollments: List[Enrollment]
