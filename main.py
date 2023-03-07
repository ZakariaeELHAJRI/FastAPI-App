from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

# create a class to define the structure of the student object
class Student(BaseModel):
    name: str
    age: int
    department: str



# create a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="fastapi-app"
)
# create a cursor to execute queries
mycursor = mydb.cursor()

app = FastAPI()


# create a get request to read the root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# create a get request to get all the students
@app.get("/students")
def get_all_students():
    sql = "SELECT * FROM students"
    mycursor.execute(sql)
    students = mycursor.fetchall()
    return students # return the array of students

# create a get request to get a student by id
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    sql = "SELECT * FROM students WHERE id = %s"
    #(student_id,) is a tuple with a single element
    val = (student_id,)
    mycursor.execute(sql, val)
    student = mycursor.fetchone()
    return student[student_id]


# create a delete request to delete a student by id
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    sql = "DELETE FROM students WHERE id = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {
        "message": "Student deleted successfully"
        }

# create a post request to add a student
@app.post("/students/add")
def add_student(student: Student):
    sql = "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)"
    val = (student.name, student.age, student.department)
    mycursor.execute(sql, val)
    mydb.commit()
    return {
        "message": "Student added successfully"
        }   

# create a put request to update a student by id
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    sql = "UPDATE students SET name = %s, age = %s, department = %s WHERE id = %s"
    val = (student.name, student.age, student.department, student_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return {
        "message": "Student updated successfully"
        }
