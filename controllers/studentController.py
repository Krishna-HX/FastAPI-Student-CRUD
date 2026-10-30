from fastapi import HTTPException

from models.studentModel import Student

students: list[Student] = []
next_id = 0


def create_student(student: Student):
    global next_id

    next_id += 1
    student.id = next_id
    students.append(student)

    return {
        "isSuccess": True,
        "message": "student created successfully",
        "student": student,
    }

# 

def get_students():
    return {
        "isSuccess": True,
        "students": students,
    }


def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return {
                "isSuccess": True,
                "student": student,
            }

    raise HTTPException(status_code=404, detail="student not found")


def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            updated_student.id = student_id 
            students[index] = updated_student

            return {
                "isSuccess": True,
                "message": "student updated successfully",
                "student": updated_student,
            }

    raise HTTPException(status_code=404, detail="Student not found")


def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)

            return {
                "isSuccess": True,
                "message": "Student deleted successfully",
                "student": deleted_student,
            }

    raise HTTPException(status_code=404, detail="Student not found")

