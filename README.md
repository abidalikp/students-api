# Students API

### List details of all students
```http
GET /api/students
```
### Create a new student
```http
POST /api/stduents
```
with json body
```json
{
    "first_name": "Abid",
    "last_name": "Ali",
    "email": "abidali@gmail.com",
    "roll_number": 1,
    "gender": "m",
    "gpa": 7.1,
    "major": 1
}
```
### List details of a student
```http
GET /api/students/1
```
### Update details of a student
```http
PATCH /api/students/1
```
with json body
```json
{
    "email": "abid@yahoo.com"
}
```
### Delete a student
```http
DELETE /api/students/1
```

### Get courses enrolled by a student
```http
GET /api/students/1/courses
```

### List details of all majors
```http
GET /api/majors
```

### Create a major
```http
POST /api/majors
```
with json body
```json
{
    "name": "Computer Science"
}
```

### List details of all courses
```http
GET /api/courses
```

### Create a course
```http
POST /api/courses
```
with json body
```json
{
    "name": "Database Management System"
}
```

### List students enrolled in a course
```http
GET /api/courses/1/students
```

### Get all student enrollment in courses
```http
GET /api/studentcourses
```

### Enroll a student in a course
```http
POST /api/studentcourses
```
with json body
```json
{
    "student": 1,
    "course": 1
}
```

---
---

# Run Locally

1. Clone this repository:
```
git clone https://github.com/abidalikp/students-api.git
```

2. Create a virtual environment:
```
py -m venv virtual
```

3. Activate virtual environment:
```
source virtual/Scripts/activate
```

4. Install requirements using pip:
```
pip install -r requirements.txt
```

5. Run django server:
```
py manage.py runserver
```

6. Test API using the base url:
```
http://localhost:8000
```

---
---

# Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 204 | `NO CONTENT` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |
