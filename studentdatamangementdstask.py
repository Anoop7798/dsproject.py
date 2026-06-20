class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        self.students[roll] = Student(roll, name, marks)
        print("Student Added Successfully!")

    def update_student(self):
        roll = input("Enter Roll No to Update: ")
        if roll in self.students:
            name = input("Enter New Name: ")
            marks = float(input("Enter New Marks: "))
            self.students[roll].name = name
            self.students[roll].marks = marks
            print("Record Updated!")
        else:
            print("Student Not Found!")

    def delete_student(self):
        roll = input("Enter Roll No to Delete: ")
        if roll in self.students:
            del self.students[roll]
            print("Record Deleted!")
        else:
            print("Student Not Found!")

    def search_student(self):
        roll = input("Enter Roll No to Search: ")
        if roll in self.students:
            self.students[roll].display()
        else:
            print("Student Not Found!")

    def display_all(self):
        if not self.students:
            print("No Records Found!")
        else:
            for student in self.students.values():
                student.display()


manager = StudentManager()

while True:
    print("\n--- Student Data Manager ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.update_student()
    elif choice == "3":
        manager.delete_student()
    elif choice == "4":
        manager.search_student()
    elif choice == "5":
        manager.display_all()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")