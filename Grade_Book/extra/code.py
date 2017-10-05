import os.path
import numpy as np
from pathlib import Path


students_data = []

class Classroom(object):
    def __init__(self, subject):
        self.subject = subject

    def classSchedule(self, class_name, date, time):
        self.class_name = class_name
        self.date = date
        self.time = time

roster_list = []

class Student(object):

    def __init__(self, name):
        self.name = name
        # print(self.name, "is added to the class")
        
    def roster(self):
        roster_list.append(self.name)
        print("Current roster list:", roster_list)

    def student_assignment(self, assigment_name, student_grade):
        self.assignemnt_name = assigment_name
        self.student_grade = student_grade
        # print(self.name, "has a", self.student_grade, "on", self.assignemnt_name)

"""
Student Rosters (objects)
list of all assigments 
grade completed assigments
grade point average 
"""

student_files = os.path.isfile("./student.npy")

# student objects
# all assienments 
# grades

# TEACHERS: add & remove students
# TEACHERS: add & remove assignemnts 

def startPlace():
    if student_files:
        print("Would you like to check, add, or remove from the roster?")
        user_choice = input()
        if user_choice == "add":
            print("Would you like to add assignements or students?")
            add_choice = input()
            if add_choice == "students":
                student_files.read()

    else:
        print("What class would you like to start?")
        class_subject = input("Subject: ")
        Classroom(class_subject)
        print("Classroom for", class_subject, "has been created!")
        print("What is the name of the classroom?")
        class_name = input("Class Name: ")
        print("What day of the week will the class be held on?")
        date = input("Day: ")
        print("What time is the class?")
        time = input("Time: ")
        Classroom(class_subject).classSchedule(class_name, date, time)
        print(class_name,"is on",date,"at",time)


        student = Student("John") 
        np.save("student.npy", student)
        student.roster()

startPlace()

