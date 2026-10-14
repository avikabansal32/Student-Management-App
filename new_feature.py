
from statistics import mean, median

# Student records:
# roll_number: [name, English, Hindi, SST, Science, Maths, percentage]

Student = {}

SUBJECTS = ["English", "Hindi", "SST", "Science", "Maths"]
PASS_MARKS = 33


def get_integer(prompt, minimum=None, maximum=None):
    """Read and validate integer input."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Enter a number less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_grade(percentage):
    """Return a grade based on the overall percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= PASS_MARKS:
        return "E"
    else:
        return "F"


def calculate_percentage(data):
    """Calculate the average of the five subject marks."""
    return mean(data[1:6])


def has_passed(data):
    """A student passes only if every subject has at least 33 marks."""
    return all(mark >= PASS_MARKS for mark in data[1:6])


def add_students():
    number = get_integer(
        "How many students do you want to add? ", minimum=1
    )

    for _ in range(number):
        print("\n--- Add Student ---")

        name = input("Enter student name: ").strip()

        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip()

        roll_number = get_integer("Enter roll number: ", minimum=1)

        if roll_number in Student:
            print("This roll number already exists. Student skipped.")
            continue

        marks = []

        for subject in SUBJECTS:
            mark = get_integer(
                f"Enter {subject} marks (0-100): ",
                minimum=0,
                maximum=100,
            )
            marks.append(mark)

        percentage = mean(marks)

        Student[roll_number] = [name] + marks + [percentage]

        print(f"Student {name} added successfully!")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {get_grade(percentage)}")
        print(
            "Result:",
            "PASS" if has_passed(Student[roll_number]) else "FAIL",
        )


def delete_student():
    if not Student:
        print("No students are available to delete.")
        return

    roll_number = get_integer(
        "Enter the roll number to delete: ", minimum=1
    )

    if roll_number in Student:
        removed = Student.pop(roll_number)
        print(f"Student {removed[0]} removed successfully.")
    else:
        print("Student not found.")


def view_student():
    if not Student:
        print("No students found.")
        return

    roll_number = get_integer(
        "Enter the roll number to view: ", minimum=1
    )

    if roll_number not in Student:
        print("Roll number not found.")
        return

    data = Student[roll_number]

    print("\n--- Student Details ---")
    print(f"Roll Number: {roll_number}")
    print(f"Name: {data[0]}")

    for subject, mark in zip(SUBJECTS, data[1:6]):
        print(f"{subject}: {mark}/100")

    percentage = calculate_percentage(data)

    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {get_grade(percentage)}")
    print(f"Result: {'PASS' if has_passed(data) else 'FAIL'}")


def check_results():
    if not Student:
        print("No students found.")
        return

    print("\n--- Student Results ---")

    for roll_number, data in Student.items():
        percentage = calculate_percentage(data)
        result = "PASS" if has_passed(data) else "FAIL"

        print(
            f"Roll: {roll_number} | "
            f"Name: {data[0]} | "
            f"Percentage: {percentage:.2f}% | "
            f"Grade: {get_grade(percentage)} | "
            f"Result: {result}"
        )


def performance_analytics():
    """Display class-level and subject-level performance statistics."""
    if not Student:
        print("\nNo student data available for analytics.")
        return

    records = []

    for roll_number, data in Student.items():
        percentage = calculate_percentage(data)

        records.append({
            "roll": roll_number,
            "name": data[0],
            "marks": data[1:6],
            "percentage": percentage,
            "passed": has_passed(data),
            "grade": get_grade(percentage),
        })

    percentages = [record["percentage"] for record in records]

    total_students = len(records)
    passed_students = sum(record["passed"] for record in records)
    failed_students = total_students - passed_students
    pass_percentage = passed_students / total_students * 100

    highest = max(percentages)
    lowest = min(percentages)

    toppers = [
        record for record in records
        if record["percentage"] == highest
    ]

    lowest_scorers = [
        record for record in records
        if record["percentage"] == lowest
    ]

    print("\n" + "=" * 45)
    print("       STUDENT PERFORMANCE ANALYTICS")
    print("=" * 45)

    # Class overview
    print("\n--- Class Overview ---")
    print(f"Total Students : {total_students}")
    print(f"Class Average  : {mean(percentages):.2f}%")
    print(f"Class Median   : {median(percentages):.2f}%")
    print(f"Highest Score  : {highest:.2f}%")
    print(f"Lowest Score   : {lowest:.2f}%")
    print(f"Students Passed: {passed_students}")
    print(f"Students Failed: {failed_students}")
    print(f"Pass Percentage: {pass_percentage:.2f}%")

    # Topper ranking, including ties
    print("\n--- Topper(s) ---")

    for record in toppers:
        print(
            f"{record['name']} "
            f"(Roll {record['roll']}) - "
            f"{record['percentage']:.2f}%"
        )

    print("\n--- Lowest Scorer(s) ---")

    for record in lowest_scorers:
        print(
            f"{record['name']} "
            f"(Roll {record['roll']}) - "
            f"{record['percentage']:.2f}%"
        )

    # Subject-wise statistics
    print("\n--- Subject-wise Performance ---")

    for index, subject in enumerate(SUBJECTS):
        subject_marks = [
            record["marks"][index] for record in records
        ]

        subject_average = mean(subject_marks)
        subject_highest = max(subject_marks)
        subject_lowest = min(subject_marks)

        print(
            f"{subject}: Average = {subject_average:.2f}, "
            f"Highest = {subject_highest}, "
            f"Lowest = {subject_lowest}"
        )

    # Grade distribution
    print("\n--- Grade Distribution ---")

    grade_order = ["A+", "A", "B", "C", "D", "E", "F"]

    for grade in grade_order:
        count = sum(
            1 for record in records
            if record["grade"] == grade
        )

        print(f"Grade {grade}: {count} student(s)")

    # Individual student summaries
    print("\n--- Individual Performance ---")

    ranked_records = sorted(
        records,
        key=lambda record: (
            -record["percentage"],
            record["roll"],
        ),
    )

    for position, record in enumerate(ranked_records, start=1):
        result = "PASS" if record["passed"] else "FAIL"

        print(
            f"{position}. {record['name']} "
            f"(Roll {record['roll']}) | "
            f"{record['percentage']:.2f}% | "
            f"Grade {record['grade']} | {result}"
        )

    print("=" * 45)


def main():
    print("---- WELCOME TO STUDENT MANAGEMENT APP ----")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View Student")
        print("4. Check Results")
        print("5. Student Performance Analytics")
        print("6. Exit")

        choice = get_integer("Enter your choice: ", minimum=1, maximum=6)

        if choice == 1:
            add_students()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            view_student()
        elif choice == 4:
            check_results()
        elif choice == 5:
            performance_analytics()
        elif choice == 6:
            print("Thank you for using the Student Management App!")
            break


if __name__ == "__main__":
    main()
