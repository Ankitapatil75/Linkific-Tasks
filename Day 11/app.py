from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample employee data
employees = [
    {
        "id": 1,
        "name": "Ankita",
        "department": "Data Science",
        "salary": 45000
    },
    {
        "id": 2,
        "name": "Rahu",
        "department": "Development",
        "salary": 50000
    }
]


# --------------------------------
# 1. Hello World API
# --------------------------------
@app.route("/")
def home():
    return "Hello World API is running!"


# --------------------------------
# 2. GET - Get all employees
# --------------------------------
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200


# --------------------------------
# 3. POST - Add a new employee
# --------------------------------
@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.get_json()

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"],
        "salary": data["salary"]
    }

    employees.append(new_employee)

    return jsonify(new_employee), 201


# --------------------------------
# 4. PUT - Update an employee
# --------------------------------
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = data.get(
                "name",
                employee["name"]
            )

            employee["department"] = data.get(
                "department",
                employee["department"]
            )

            employee["salary"] = data.get(
                "salary",
                employee["salary"]
            )

            return jsonify(employee), 200

    return jsonify({
        "error": "Employee not found"
    }), 404


# --------------------------------
# 5. DELETE - Delete an employee
# --------------------------------
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return jsonify({
                "message": "Employee deleted successfully"
            }), 200

    return jsonify({
        "error": "Employee not found"
    }), 404


# --------------------------------
# Run Flask application
# --------------------------------
if __name__ == "__main__":
    app.run(debug=True)