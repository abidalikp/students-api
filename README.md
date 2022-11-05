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
