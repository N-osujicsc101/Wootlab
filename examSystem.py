def main():
    print("Welcome to CESS (Console Examination Scoring System)!!\n")

    studentRecords = []

    while True:
        user_choice = input("Which user are you? \n1.Teacher \n2.Student\n3. Quit\n ")

        if user_choice == "1":
            teacher(studentRecords)
        elif user_choice == "2":
            student(studentRecords)
        elif user_choice == "3":
            break
        else:
            print("Invalid input!!")


def teacher(studentRecords):
    print("Welcome Teacher!!")

    while True:
        teacher_choice = input(
            "Enter your choice?\n1.Update student result\n2.View student result\n3.Delete student result\n4.Back\n "
        )

        if teacher_choice == "1":
            update_result(studentRecords)
        elif teacher_choice == "2":
            view_result(studentRecords)
        elif teacher_choice == "3":
            delete_result(studentRecords)
        elif teacher_choice == "4":
            return
        else:
            print("Invalid entry!!")


def update_result(studentRecords):
    studentId = input("Enter student Id: ")
    studentName = input("Enter student Name: ")

    for student in studentRecords:
        if student.get("Student Id") == studentId:
            print("Student ID already exists. Updating scores...")
            subjects = {
                "Math": student.get("Math", "N/A"),
                "English": student.get("English", "N/A"),
                "Theology": student.get("Theology", "N/A"),
                "Philosophy": student.get("Philosophy", "N/A"),
                "Intro to Programming": student.get("Intro to Programming", "N/A"),
            }

            while True:
                studentResult = input(
                    "These are the subjects the student is taking\n1.Math\n2.English\n3.Theology\n4.Philosophy\n5.Intro to Programming\n"
                )

                if studentResult == "1":
                    subjects["Math"] = int(input("Enter score: "))
                elif studentResult == "2":
                    subjects["English"] = int(input("Enter score: "))
                elif studentResult == "3":
                    subjects["Theology"] = int(input("Enter score: "))
                elif studentResult == "4":
                    subjects["Philosophy"] = int(input("Enter score: "))
                elif studentResult == "5":
                    subjects["Intro to Programming"] = int(input("Enter score: "))
                    break
                else:
                    print("Invalid entry!!")

            student.update(
                {"Student Id": studentId, "Student Name": studentName, **subjects}
            )
            print(f"{studentName}'s record has been updated\n")
            return

    print("Student ID does not exist. Creating new record...\n")
    subjects = {
        "Math": "N/A",
        "English": "N/A",
        "Theology": "N/A",
        "Philosophy": "N/A",
        "Intro to Programming": "N/A",
    }

    while True:
        studentResult = input(
            "These are the subjects the student is taking\n1.Math\n2.English\n3.Theology\n4.Philosophy\n5.Intro to Programming\n"
        )

        if studentResult == "1":
            subjects["Math"] = int(input("Enter score: "))
        elif studentResult == "2":
            subjects["English"] = int(input("Enter score: "))
        elif studentResult == "3":
            subjects["Theology"] = int(input("Enter score: "))
        elif studentResult == "4":
            subjects["Philosophy"] = int(input("Enter score: "))
        elif studentResult == "5":
            subjects["Intro to Programming"] = int(input("Enter score: "))
            break
        else:
            print("Invalid entry!!")

    studentRecords.append(
        {"Student Id": studentId, "Student Name": studentName, **subjects}
    )
    print(f"{studentName}'s record has been added\n")


def view_result(studentRecords):
    if not studentRecords:
        print("No student records found.")
        return

    for i, student in enumerate(studentRecords, start=1):
        studentName = student.get("Student Name", "Unknown")
        Result = {
            "Math": student.get("Math", "N/A"),
            "English": student.get("English", "N/A"),
            "Theology": student.get("Theology", "N/A"),
            "Philosophy": student.get("Philosophy", "N/A"),
            "Intro to Programming": student.get("Intro to Programming", "N/A"),
        }
        print(f"{i}. {student.get('Student Id', 'Unknown')}, {studentName}, {Result}\n")


def delete_result(studentRecords):
    if not studentRecords:
        print("No student records found.")
        return
    studentId = input("Enter student Id: ")
    for i, student in enumerate(studentRecords):
        if student.get("Student Id") == studentId:
            studentName = student.get("Student Name", "Unknown")
            del studentRecords[i]
            print(f"{studentName}'s record has been deleted\n")
            return
    print("Student not found.\n")


def student(studentRecords):
    while True:
        print("Welcome Student!!")
        student_choice = input("What is your Student Id: ")

        for student in studentRecords:
            if student.get("Student Id") == student_choice:
                studentName = student.get("Student Name", "Unknown")
                print(f"Hello {studentName}")
                Result = {
                    "Math": student.get("Math", "N/A"),
                    "English": student.get("English", "N/A"),
                    "Theology": student.get("Theology", "N/A"),
                    "Philosophy": student.get("Philosophy", "N/A"),
                    "Intro to Programming": student.get("Intro to Programming", "N/A"),
                }
                print(
                    f"Student Id: {student.get('Student Id', 'Unknown')}, Name: {studentName}, Results: {Result}\n"
                )
                break
        else:
            print("Student not found.\n")

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break


if __name__ == "__main__":
    main()
