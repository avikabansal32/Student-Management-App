def Student(self, name, roll_num, english, hindi, sst, maths, science):
    self.name = name
    self.rol_num = roll_num
    self.english = english
    self.hindi = hindi
    self.sst = sst
    self.sci = science
    self.maths = maths 
    def total(self):
        total = (self.english + self.hindi + self.sst + self.sci + self.maths) / 5
        return total
    print(f"Percentage of", {self.name},"Roll Number", {self.roll_num}, "is", {total})

print(f"----WELCOME TO STUDENT MANAQGEMENT APP----", "\nWhat would you like to do ?")

while True:
    print(f"1) Add Student", "\n2) Delete Student","3)Veiw Student", "\n4)Check Result", "\n5) Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter the number of student you want to add: "))
        for i in range(1, number + 1):
            name = input("Enter name of the student: ")
            roll_num = int(input("Enter the roll number: "))
            english = int(input("English marks: "))
            hindi = int(input("Hindi marks: "))
            sst = int(input("S.S.T marks: "))
            sci = int(input("Science marks: "))
            maths = int(input("Maths marks: "))
            print("Student added")
        student = Student(name, roll_num, english, hindi, sst, sci, maths)

    if choice == 2:
        number = int(input("Enter the roll number of student you want to remove: ")) 
        for student in Student:
            if number == Student(roll_no):
                Student.remove(student)

        else:
            print("Student not found")
