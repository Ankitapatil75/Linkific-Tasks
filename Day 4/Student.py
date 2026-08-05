import numpy as np

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input(f"Enter marks of Student {i+1}: "))
    marks.append(mark)

marks = np.array(marks)

print("\nHighest :", np.max(marks))

print("Lowest :", np.min(marks))

print("Average :", np.mean(marks))

print("\nStudents Above Average:")

for i in range(len(marks)):
    if marks[i] > np.mean(marks):
        print(f"Student {i+1}: {marks[i]}")