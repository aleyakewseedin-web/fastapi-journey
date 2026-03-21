import asyncio
from fastapi import APIRouter, HTTPException
from models import Enrollment
from models  import Student
from typing import List

enrollment=APIRouter()

students: List[Student] = [
    Student(
        id=1,
        name="Alice",
        major="Computer Science",
        enrollments=[
            Enrollment(course_name="Databases", semester= Semester.fall, grade=88,instructor="Dr. Smith"  ), # type: ignore
            Enrollment(course_name="Algorithms", semester = Semester.spring, grade=92) # type: ignore
        ]
    ),
    Student(
        id=2,
        name="Bob",
        major="Engineering",
        enrollments=[]
    )]
@enrollment.post("/students/")
async def create_student(student: Student):
    if not student.name or not student.department:
        raise HTTPException(status_code=400, detail="Invalid student data")
    student_id= max([s.id for s in students]) + 1 if students else 1
    new_student= Student(id=student_id, 
                         name=student.name, 
                         major=student.major, 
                         enrollments=student.enrollments)
    await asyncio.sleep(1)
    students.append(new_student) 
    return {"message": "Student created successfully", "student": new_student}




@enrollment.get("/students", response_model=List[Student])
async def get_students():
    await asyncio.sleep(1)
    return students


@enrollment.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail=f"Student with this ID {student_id} is not found")

@enrollment.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student.id==student_id:
            student.name= updated_student.name
            student.major= updated_student.major
            student.enrollments= updated_student.enrollments
            return student
    raise HTTPException(status_code=404, detail=f"Student with this ID {student_id} is not found")

@enrollment.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Student with this ID {student_id} is not found")