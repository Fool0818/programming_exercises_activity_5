highest_student_name = ""
highest_student_gwa = 0.0

with open("students.txt", "r") as student_file:
    for student_record in student_file:
        student_data = student_record.strip().split(",")

        student_name = student_data[0]
        student_gwa = float(student_data[1])

        if highest_student_gwa == 0.0 or student_gwa < highest_student_gwa:
            highest_student_name = student_name
            highest_student_gwa = student_gwa

print("Student with the highest GWA:")
print(highest_student_name, highest_student_gwa)