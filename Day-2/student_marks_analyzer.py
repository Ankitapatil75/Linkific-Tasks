# student_marks_analyzer.py

def get_marks():
    marks = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        mark = float(input(f"Enter marks of Student {i+1}: "))
        marks.append(mark)

    return marks


def calculate_statistics(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    return highest, lowest, average


def students_above_average(marks, average):
    print("\nStudents scoring above average:")

    found = False
    for i in range(len(marks)):
        if marks[i] > average:
            print(f"Student {i+1}: {marks[i]}")
            found = True

    if not found:
        print("No students scored above average.")


def display_result(highest, lowest, average):
    print("\n------ Result ------")
    print("Highest Marks :", highest)
    print("Lowest Marks  :", lowest)
    print("Average Marks :", round(average, 2))


def main():
    marks = get_marks()

    highest, lowest, average = calculate_statistics(marks)

    display_result(highest, lowest, average)

    students_above_average(marks, average)


main()