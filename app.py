# app.py
import os

def generate_academic_report():
    print("Processing Student Management & Academic Performance Data...")
    
    # Mock data representing academic records
    students = [
        {"id": "S01", "name": "Alice", "gpa": 3.8},
        {"id": "S02", "name": "Bob", "gpa": 2.9},
        {"id": "S03", "name": "Charlie", "gpa": 3.5},
        {"id": "S04", "name": "David", "gpa": 3.1},
        {"id": "S05", "name": "Eva", "gpa": 4.0}
    ]
    
    total_students = len(students)
    total_gpa = sum(student["gpa"] for student in students)
    avg_gpa = round(total_gpa / total_students, 2)
    
    # Logic: Passing criteria is a GPA >= 3.0
    passing_students = sum(1 for student in students if student["gpa"] >= 3.0)
    pass_rate = round((passing_students / total_students) * 100, 2)

    # Write metrics cleanly to an artifact text file
    filename = "report.txt"
    with open(filename, "w") as f:
        f.write("==================================================\n")
        f.write("   STUDENT MANAGEMENT & PERFORMANCE REPORT        \n")
        f.write("==================================================\n")
        f.write(f"Total Enrolled Students : {total_students}\n")
        f.write(f"Average System GPA      : {avg_gpa} / 4.0\n")
        f.write(f"Passing Students Count  : {passing_students}\n")
        f.write(f"System Passing Rate     : {pass_rate}%\n")
        f.write("==================================================\n")
        f.write("Status: Academic Evaluation Complete. Clean Execution.\n")
        
    print(f"Success: {filename} generated with precise logic.")

if __name__ == "__main__":
    generate_academic_report()
