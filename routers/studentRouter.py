from fastapi import APIRouter

from models.studentModel import Student
from controllers import studentController

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("", status_code=201)
def create_student(student: Student):
    return studentController.create_student(student)


@router.get("")
def get_students():
    return studentController.get_students()


@router.get("/{student_id}")
def get_student(student_id: int):
    return studentController.get_student(student_id)


@router.put("/{student_id}")
def update_student(student_id: int, updated_student: Student):
    return studentController.update_student(student_id, updated_student)


@router.delete("/{student_id}")
def delete_student(student_id: int):
    return studentController.delete_student(student_id)
