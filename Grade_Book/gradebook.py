import os
import numpy as np
from pathlib import Path
import Classroom
from Classroom import Classroom
import Students
import roster
import Assignments


def precheck():
    if any(classroom_db.startswith('classroom_') for classroom_db in os.listdir('./db/')):
        print("Would you like to view students or assignemnts?")
        student_or_assignments = input("--> ")
        if student_or_assignments == "students" or "student":
            print("Do you want to edit student roster or view Grades?")
            edit_or_grades = input("--> ")
            if edit_or_grades == "edit" or "edit student roster":
                roster.roster_options()
    else:
        print("Hi, there's no classrooms yet. Let's create one!")
        classroom_name = input("Classroom Name: ")
        with open('./db/classroom_' + classroom_name + '.txt', 'a') as classroom_db:
            classroom_db.write("\n")    
        created_class = Classroom(classroom_name)
        print(classroom_name, "has been created.")
        class_schedule(created_class, classroom_name)
        return created_class, classroom_name

def class_schedule(created_class, classroom_name):
    print("What day is the class held on?")
    class_date = input("Day: ")
    print("What time does class start?")
    class_time = input("Time: ")
    created_class.class_schedule(class_date, class_time)
    print(classroom_name, "will be on", class_date, "at", class_time)


def start():
    precheck()
    



start()





