# employee_salary.py

employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    employees[emp_id] = {
        "name": name,
        "salary": basic_salary
    }

def calculate_salary(salary):
    hra = salary * 0.20
    da = salary * 0.10
    total = salary + hra + da
    return total

def display_employees():
    print("\nEmployee Salary Details")

    if len(employees) == 0:
        print("No Employee Records")
        return

    for emp_id, details in employees.items():
        total = calculate_salary(details["salary"])

        print("------------------------")
        print("Employee ID :", emp_id)
        print("Name        :", details["name"])
        print("Basic Salary:", details["salary"])
        print("Net Salary  :", total)

while True:
    print("\nEmployee Salary System")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")