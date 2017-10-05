from Students import Student

def add_student():
        print("What is the student's name?")
        student_name = input("Student Name: ")
        Student(student_name)
        
def remove_student():
    print("Which student would you like to remove?")
    remove_choice = input("Remove: ")
    with open('./db/students.txt', 'r+') as student_db:
        student_names = [line.strip() for line in student_db]
        if remove_choice in student_names:
            t = student_db.read()
            student_db.seek(0)
            for line in t.split('\n'):
                if line != remove_choice:
                    student_db.write(line + '\n')
            student_db.truncate()
            print(remove_choice, "has been removed from the roster")
        else: 
            print(remove_choice, "is not in the roster")
            start()

def roster_options():
    print("Would you like to check, add, or remove from the roster?")
    user_choice = input("--> ")
    if user_choice == "add":
        add_student()
    elif user_choice == "remove":
        remove_student()
    elif user_choice == "check":
        with open('./db/students.txt', 'r') as student_db:
            student_names = [line.strip() for line in student_db]
            print(', '.join(student_names))



    #     print("What class would you like to start?")
    #     class_subject = input("Subject: ")
    #     Classroom(class_subject)
    #     print("Classroom for", class_subject, "has been created!")
    #     print("What is the name of the classroom?")
    #     class_name = input("Class Name: ")
    #     print("What day of the week will the class be held on?")
    #     date = input("Day: ")
    #     print("What time is the class?")
    #     time = input("Time: ")
    #     Classroom(class_subject).classSchedule(class_name, date, time)
    #     print(class_name,"is on",date,"at",time)