Student = {}
print("----WELCOME TO STUDENT MANAQGEMENT APP----", "\nWhat would you like to do ?")

while True:
    print(f"1) Add Student", "\n2) Delete Student","\n3)Veiw Student", "\n4)Check Result", "\n5) Exit")
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
            total = (english + hindi + sst + sci + maths) / 5
            print("Total percentage of", {name}, "is", {total})
            print("Student added")
            Student[roll_num] = [name, english, hindi, sst, sci, maths, total]

    elif choice == 2:
        roll_num = int(input("Enter the roll number of student you want to remove: ")) 
        if roll_num in Student[roll_num]:    
            del Student[roll_num]
            print("Student removed Successfully")

        else:
            print("Student not found")

    elif choice == 3:
        roll_num = int(input("Enter the roll number of student you want to veiw: "))
        if roll_num in Student:
            print(Student[roll_num])
        else:
            print("Roll number invalid.")

    elif choice == 4:
       if len(Student) == 0:
        print("No students found")
    
       else:
            for roll_num, data in Student.items():
             print("Name:", data[0], "| Percentage:", data[6], "%")     
    
    elif choice == 5:
        print("----THANK YOU FOR VISITING!!<3<3----")
        break