from pydantic import BaseModel, Field, model_validator, model_validator
from enum import Enum
from typing import Optional

class Semester(str, Enum):
    fall = "Fall"
    spring = "Spring"
    summer = "Summer"

class Enrollment(BaseModel):
    course_name: str=Field(min_length=2, max_length=100,)
    semester: Semester
    grade: float = Field (ge=0.0, le=100.0)  # Grade should be between 0.0 and 100.0
    instructor: Optional[str] = Field(default=None, min_length=2, max_length=50)

  
    @model_validator(mode="after")
    def check_grade(cls, values):
        if values.grade < 50:
            raise ValueError("Student must pass the course")
        return values