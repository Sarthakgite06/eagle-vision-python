class Student:

    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.age = 0
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0

    def menu(self):

        print("\n1. Student 1 Details")
        print("2. Student 1 Total")
        print("3. Student 1 Percentage")
        print("4. Student 1 Result")
        print("5. Student 1 Update Marks")

        print("6. Student 2 Details")
        print("7. Student 2 Total")
        print("8. Student 2 Percentage")
        print("9. Student 2 Result")
        print("10. Student 2 Update Marks")

        print("11. Exit")

    def enter_details(self):

        self.name = input("Enter name of student: ")
        self.roll_no = int(input("Enter roll no: "))
        self.age = int(input("Enter age: "))

        self.marks1 = int(input("Enter Marks of Python: "))
        self.marks2 = int(input("Enter Marks of Java: "))
        self.marks3 = int(input("Enter Marks of SQL: "))

        print("Student details added successfully")

    def display_details(self):

        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Age:", self.age)
        print("Python Marks:", self.marks1)
        print("Java Marks:", self.marks2)
        print("SQL Marks:", self.marks3)

    def calculate_total(self):

        total_mark = self.marks1 + self.marks2 + self.marks3

        print("\nTotal Marks:", total_mark)

    def calculate_percentage(self):

        total_mark = self.marks1 + self.marks2 + self.marks3

        percentage = total_mark / 3

        print("\nPercentage:", percentage, "%")

    def check_result(self):

        if self.marks1 >= 35 and self.marks2 >= 35 and self.marks3 >= 35:

            print("Result: PASS")

        else:

            print("Result: FAIL")

            if self.marks1 < 35:
                print("Failed in Python")

            if self.marks2 < 35:
                print("Failed in Java")

            if self.marks3 < 35:
                print("Failed in SQL")

    def update_marks(self):

        print("\n1. Python")
        print("2. Java")
        print("3. SQL")

        subject = int(input("Enter subject number: "))
        new_marks = int(input("Enter new marks: "))

        match subject:

            case 1:
                self.marks1 = new_marks
                print("Python marks updated:", self.marks1)

            case 2:
                self.marks2 = new_marks
                print("Java marks updated:", self.marks2)

            case 3:
                self.marks3 = new_marks
                print("SQL marks updated:", self.marks3)

            case _:
                print("Invalid subject number")

student1 = Student()
student2 = Student()

student1.enter_details()

student2.enter_details()

while True:

    student1.menu()

    user_input = input("\nEnter your choice: ")

    if user_input.isdigit():
        choice = int(user_input)
    else:
        print("Please enter a valid number")
        continue

    match choice:

        case 1:
            student1.display_details()

        case 2:
            student1.calculate_total()

        case 3:
            student1.calculate_percentage()

        case 4:
            student1.check_result()

        case 5:
            student1.update_marks()

        case 6:
            student2.display_details()

        case 7:
            student2.calculate_total()

        case 8:
            student2.calculate_percentage()

        case 9:
            student2.check_result()

        case 10:
            student2.update_marks()

        case 11:
            print("Thank you for using Student Management System")
            break

        case _:
            print("Invalid choice")