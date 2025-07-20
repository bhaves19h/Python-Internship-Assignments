num_students = int(input("Enter number of students: "))

students = []

for i in range(num_students):
    name = input(f"\nEnter name of student {i + 1}: ")
    marks = []

    for j in range(1, 4):
        mark = float(input(f"Enter mark for subject {j}: "))
        marks.append(mark)

    average = sum(marks) / 3
    students.append({
        'name': name,
        'marks': marks,
        'average': average
    })


print("\nStudent Records:")
for student in students:
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Average Marks: {student['average']:.2f}\n")
