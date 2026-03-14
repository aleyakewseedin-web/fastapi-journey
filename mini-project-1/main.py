import asyncio
from fastapi import FastAPI
from typing import List
from mini_project_1.models import student,enrollment


app= FastAPI()  

students: List[student] = [
    student(
        id=1,
        name="Alice",
        major="Computer Science",
        enrollments=[
            mini_project_1.models.enrollment(course_name="Databases", semester= Semester.fall, grade=88,instructor="Dr. Smith"  ), # type: ignore
            mini_project_1.models.enrollment(course_name="Algorithms", semester = Semester.spring, grade=92) # type: ignore
        ]
    ),
    student(
        id=2,
        name="Bob",
        department="engineering",
        enrollments=[]
    )]
@app.post("/students/")
async def create_student(student: student):
    student_id= max([s.id for s in student]) + 1 if student else 1
    new_student= student(id=student_id, name=student.name, department=student.department, enrollments=student.enrollments)
    await asyncio.sleep(1)
    student.append(new_student) 
    return {"message": "Student created successfully", "student": new_student}


@app.get("/students", response_model=List[student])
async def get_students():
    await asyncio.sleep(1)
    return students

@app.get("/students/{student_id}", response_model=student)
async def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}

@app.put("/students/{student_id}", response_model=student)
async def update_student(student_id: int, updated_student: student):
    for student in students:
        if student.id==student_id:
            student.name= updated_student.name
            student.department= updated_student.department
            student.enrollments= updated_student.enrollments
            return student
        
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}
    return {"error": "Student not found"}