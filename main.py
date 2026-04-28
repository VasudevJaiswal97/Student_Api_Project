from fastapi import FastAPI
import json

app = FastAPI()

FILE = "students.json"

def read_students():
    with open(FILE , "r") as f:
        return json.load(f)
    
def write_students(data):
    with open(FILE , "w") as f:
        json.dump(data , f , indent = 4)

@app.get("/")
def home():
    return {"message":"Welcome to Student API"}

@app.get("/students")
def get_all_students():
    students = read_students()
    return students

@app.post("/students")
def add_students(student : dict):
    students = read_students()
    students.append(student)
    write_students(students)
    return {"message" : "student added successfully"}

@app.get("/students/{id}")
def get_student_by_id(id: int):
    students = read_students()

    for student in students:
        if student["id"] == id:
            return student
    return {"message" : "Student Not Found"}


@app.put("/students/{id}")
def update_student(id: int, new_student: dict):
    students = read_students()

    for student in students:
        if student["id"] == id:
            student.update(new_student)
            write_students(students)
            return {"message": "Student Updated Successfully"}
        
@app.delete("/student/{id}")
def delete_student(id: int):
    students = read_students()

    for student in students:
        if student["id"] == id:
            students.remove(student)
            write_students(students)
            return {"message": "Student deleted successfully"}

    return {"message" : "Student not found"}