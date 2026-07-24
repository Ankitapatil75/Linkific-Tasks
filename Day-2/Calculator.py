# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Answer:", add(a, b))
    elif choice == 2:
        print("Answer:", subtract(a, b))
    elif choice == 3:
        print("Answer:", multiply(a, b))
    elif choice == 4:
        print("Answer:", divide(a, b))
    else:
        print("Invalid Choice")