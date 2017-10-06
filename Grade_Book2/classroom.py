from students import Student

class Classroom(object):
    def __init__(self, name):
        self.name = name
        self.student_roster = {}
        self.assignment_roster = []

    def class_schedule(self, date, time):
        self.class_date = date
        self.class_time = time
        print(self.name, "is on", self.class_date, "at", self.class_time)

    def add_student(self, name, ID):
        student = Student(name, ID)
        self.student_roster[name] = ID

    def remove_student(self, name):
        del self.student_roster[name]
        print(name, "has been removed from the roster for the", self.name, "class")

    def get_student_roster(self):
        print(self.student_roster)

    def add_assignment(self, name):
        self.assignment_roster.append(name)
    
    def remove_assignment(self, name):
        self.assignment_roster.remove(name)