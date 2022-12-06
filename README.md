# **Students API**

## **Table of Contents**
| No. | [Endpoints](#endpoints) |
| --- | --- |
| 1 | [List details of all students](#list-details-of-all-students) |
| 2 | [Create a new student](#create-a-new-student) |
| 3 | [List details of a student](#list-details-of-a-student) |
| 4 | [Update details of a student](#update-details-of-a-student) |
| 5 | [Delete a student](#delete-a-student) |
| 6 | [Get courses enrolled by a student](#get-courses-enrolled-by-a-student) |
| 7 | [List details of all majors](#list-details-of-all-majors) |
| 8 | [Create a major](#create-a-major) |
| 9 | [List details of a major](#list-details-of-a-major) |
| 10 | [Update details of a major](#update-details-of-a-major) |
| 11 | [Delete a major](#delete-a-major) |
| 12 | [List courses in a major](#list-courses-in-a-major) |
| 13 | [List students in a major](#list-students-in-a-major) |
| 14 | [List details of all courses](#list-details-of-all-courses) |
| 15 | [Create a course](#create-a-course) |
| 16 | [List students enrolled in a course](#list-students-enrolled-in-a-course) |
| 17 | [List all student enrollment in courses](#list-all-student-enrollment-in-courses) |
| 18 | [Enroll a student in a course](#enroll-a-student-in-a-course) |
|  | **[Run Locally](#run-locally)** |
|  | **[Status Codes](#status-codes)** |


---
[Back to Top ⬆ ](#table-of-contents)

---

## **Endpoints**

1. ###  List details of all students

```http
GET /api/students
```

2. ### Create a new student

```http
POST /api/stduents
```

- with json body

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

3. ### List details of a student

```http
GET /api/students/1
```

4. ### Update details of a student

```http
PATCH /api/students/1
```

- with json body

```json
{
    "email": "abid@yahoo.com"
}
```

5. ### Delete a student

```http
DELETE /api/students/1
```

6. ### Get courses enrolled by a student

```http
GET /api/students/1/courses
```

---
[Back to Top ⬆ ](#table-of-contents)

---

7. ### List details of all majors

```http
GET /api/majors
```

8. ### Create a major

```http
POST /api/majors
```

- with json body

```json
{
    "name": "Computer Science"
}
```

9. ### List details of a major

```http
GET /api/majors/1
```

10. ### Update details of a major

```http
PATCH /api/majors/1
```

- with json body

```json
{
    "name": "Computer Science"
}
```

11. ### Delete a major

```http
DELETE /api/majors/1
```

12. ### List courses in a major

```http
GET /api/majors/1/courses
```

13. ### List students in a major

```http
GET /api/majors/1/students
```

---
[Back to Top ⬆ ](#table-of-contents)

---

14. ### List details of all courses

```http
GET /api/courses
```

15. ### Create a course

```http
POST /api/courses
```

- with json body

```json
{
    "name": "Database Management System"
}
```

16. ### List students enrolled in a course

```http
GET /api/courses/1/students
```

17. ### List all student enrollment in courses

```http
GET /api/studentcourses
```

18. ### Enroll a student in a course

```http
POST /api/studentcourses
```

- with json body

```json
{
    "student": 1,
    "course": 1
}
```

---
[Back to Top ⬆ ](#table-of-contents)

---

## **Run Locally**

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
[Back to Top ⬆ ](#table-of-contents)

---

## **Status Codes**

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 204 | `NO CONTENT` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

---
[Back to Top ⬆ ](#table-of-contents)

---