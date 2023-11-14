# Function to input student records
def input_student_records():
    n = int(input("Enter the number of students: "))
    records = []

    for i in range(n):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter total marks (out of 100): "))
        records.append({"Name": name, "Roll No": roll_no, "Total Marks": marks, "Rank": 0})

    return records

# Function to display details of the student with maximum marks
def display_max_marks_student(records):
    max_marks_student = max(records, key=lambda x: x["Total Marks"])
    print("\nDetails of the student with maximum marks:")
    print("Name:", max_marks_student["Name"])
    print("Roll No:", max_marks_student["Roll No"])
    print("Total Marks:", max_marks_student["Total Marks"])

# Function to add rank to each student record
def add_rank(records):
    records.sort(key=lambda x: x["Total Marks"], reverse=True)
    for i in range(len(records)):
        records[i]["Rank"] = i + 1

# Function to display student details in ascending order of their ranks
def display_students_by_rank(records):
    print("\nStudent details in ascending order of ranks:")
    for student in sorted(records, key=lambda x: x["Rank"]):
        print("Rank:", student["Rank"])
        print("Name:", student["Name"])
        print("Roll No:", student["Roll No"])
        print("Total Marks:", student["Total Marks"])
        print()

# Main program
student_records = input_student_records()
display_max_marks_student(student_records)
add_rank(student_records)
display_students_by_rank(student_records)
