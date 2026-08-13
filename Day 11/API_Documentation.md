# Employee REST API Documentation

## Base URL

http://127.0.0.1:5000

---

## 1. Hello World API

### Method
GET

### Endpoint
/

### Description
Checks whether the Flask API is running.

### Response

Hello World API is running!

### Status Code
200 OK

---

## 2. Get Employees

### Method
GET

### Endpoint
/employees

### Description
Returns all employees.

### Response

[
    {
        "id": 1,
        "name": "Ankita",
        "department": "Data Science",
        "salary": 45000
    }
]

### Status Code
200 OK

---

## 3. Add Employee

### Method
POST

### Endpoint
/employees

### Request Body

{
    "name": "Priya",
    "department": "HR",
    "salary": 40000
}

### Response

{
    "id": 3,
    "name": "Priya",
    "department": "HR",
    "salary": 40000
}

### Status Code
201 Created

---

## 4. Update Employee

### Method
PUT

### Endpoint
/employees/<employee_id>

### Request Body

{
    "name": "Ankita Patil",
    "department": "AI/ML",
    "salary": 55000
}

### Status Code
200 OK

---

## 5. Delete Employee

### Method
DELETE

### Endpoint
/employees/<employee_id>

### Response

{
    "message": "Employee deleted successfully"
}

### Status Code
200 OK