student_name_list = ["Uzair", "Salman", "Ahmed Ali", "Ayaz Khan", "Shahid Khan"]

i = 0
print("\You can check the grades of these names:")
while i < len(student_name_list):
    print(student_name_list[i])
    i += 1

while True:
    student_name = input("\nEnter the Name of Student: ").lower()

    if student_name in (name.lower() for name in student_name_list):

        subject_1 = float(input("\nEnter the English Marks Here: "))
        subject_2 = float(input("Enter the Math Marks Here: "))
        subject_3 = float(input("Enter the Islamiyat Marks Here: "))

        average_marks = (subject_1 + subject_2 + subject_3) / 3

        if average_marks >= 90:
            grade = "Grade A"
        elif average_marks >= 80:
            grade = "Grade B"
        elif average_marks >= 70:
            grade = "Grade C"
        elif average_marks >= 60:
            grade = "Grade D"
        else:
            grade = "Grade F"

        print(f"\nYour Name is: {student_name.capitalize()}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Your grade is: {grade}")

    else:
        print("The Student Name is not in the Student List")