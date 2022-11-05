# Students API

### List all Students
```http
GET /api/countries
```
### Create a new student
```http
POST /api/countries
```
with json body
```json
{
    "name": "Abid Ali KP",
    "email": "abid@gmail.com",
    "roll_number": 1,
    "gender": "m",
    "percentage": 90.0
}
```
### List student details
```http
GET /api/countries/1
```
### Update student detail
```http
PATCH /api/countries/1
```
with json body
```json
{
    "email": "abid@yahoo.com"
}
```
### Delete student
```http
DELETE /api/countries/1
```

# Run Locally

1. Clone this repository:
```
git clone https://github.com/abidalikp/countries-api.git
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

6. Go to postman and test-api using the base url:
```
http://localhost:8000
```

# Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |
