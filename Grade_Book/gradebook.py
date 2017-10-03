import os
import numpy as np
from pathlib import Path

student_list = os.path.isfile("./students.txt")

class Student(object):

    def __init__(self, name):
        self.name = name
        if student_list:
            with open('students.txt', 'r') as student_db:
                student_names = [line.strip() for line in student_db]
                if self.name in student_names:
                    print(self.name, "is already in roster")
                else:
                    with open('students.txt', 'a') as student_db:
                        student_db.write(self.name + "\n")    
                        print(self.name, "is added to the roster")             
        else:
            f=open("students.txt", "a+")
            print("student data created")
            print("Current Roster: ", ', '.join(student_names))



"""
Student Rosters (objects)
list of all assigments 
grade completed assigments
grade point average 
"""
# Student("Mike")
# Student("Sam")
# 

# student objects
# all assienments 
# grades

# TEACHERS: add & remove students
# TEACHERS: add & remove assignemnts 

def start():
    print("Would you like to check, add, or remove from the roster?")
    user_choice = input("--> ")
    if user_choice == "add":
        print("Would you like to add assignements or students?")
        add_choice = input("Add: ")
        if add_choice == "students" or "student":
            print("What is the student's name?")
            student_name = input("Student Name: ")
            Student(student_name)
    elif user_choice == "remove":
        print("Which student would you like to remove?")
        with open('students.txt', 'r+') as student_db:
            t = student_db.read()
            student_db.seek(0)
            remove_choice = input("Remove: ")
            for line in t.split('\n'):
                if line != remove_choice:
                    student_db.write(line + '\n')
            student_db.truncate()

        # with open('students.txt', 'w') as student_db:
        #     student_db.replace(remove_choice, "")
            print(remove_choice, "has been removed from the roster")
    # else:
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


    #     student = Student("John") 
    #     np.save("student.npy", student)
    #     student.roster()

start()

