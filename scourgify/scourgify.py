import csv

first_file = "before.csv"
second_file = "after.csv"

students = []
new_students = []

with open(first_file) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row["name"].split(","))
    for student in students:
        student = student[::-1]
        student_first_name, student_last_name = student[0].lstrip(), student[1].lstrip()
        new_students.append([student_first_name, student_last_name])
    
    for n in new_students:
        print(n)
    
with open(second_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last"])
    for n in new_students:
        writer.writerow({"first": n[0], "last": n[1]})

 