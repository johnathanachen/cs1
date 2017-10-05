import os
student_list = os.path.isfile("./db/students.txt")

class Student(object):
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.grade_average = None
        self.assignments = {}
        if student_list:
            with open('./db/students.txt', 'r') as student_db:
                student_names = [line.strip() for line in student_db]
                if self.name in student_names:
                    print(self.name, "is already in roster.")
                else:
                    with open('./db/students.txt', 'a') as student_db:
                        student_db.write(self.name + "\n")
                        print(self.name, "has been added to the roster.")              
        else:
            f=open("./db/students.txt", "a+")
            print("student data created")
            print("Current Roster: ", ', '.join(student_names))


    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade


    def delete_assignment(self, assignment_name):
        del self.assignments[assignment_name]
        

# remove and add grades
