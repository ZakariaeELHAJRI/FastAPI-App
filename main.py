from fastapi import FastAPI

app = FastAPI()
# create  simple array of students contanint name , age , department
students = [
    {
        "name": "John",
        "age": 20,
        "department": "Computer Science"
    },
    {
        "name": "Jane",
        "age": 21,
        "department": "Information Technology"
    },
    {
        "name": "Jack",
        "age": 22,
        "department": "Electrical Engineering"
    }
]
# create a get request to read the root
@app.get("/")
def read_root():
    return {"Hello": "World"}
# create a get request to get all the students
@app.get("/students")
def get_all_students():
    return students # return the array of students

# create a get request to get a student by id
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    return students[student_id]


# create a delete request to delete a student by id
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students.pop(student_id)
    return {
        "message": "Student deleted successfully",
        "new list ": students
        }
# create a post request to add a student
@app.post("/students/add")
def add_student(student: dict):
    students.append(student)
    return {
        "message": "Student added successfully",
        "new list ": students
        }   
# create a put request to update a student by id
@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    students[student_id] = student
    return {
        "message": "Student updated successfully",
        "new list ": students
        }
#t