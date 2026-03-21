import asyncio
from fastapi import FastAPI, HTTPException
from typing import List
from models import Student
from models.enrollment import Semester
from models.enrollment import Enrollment


app= FastAPI()  


