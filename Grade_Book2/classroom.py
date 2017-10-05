class Classroom(object):
    def __init__(self, name):
        self.name = name
        self.student_roster = []
        self.assignment_roster = []

    def class_schedule(self, date, time):
        self.class_date = date
        self.class_time = time

    def add_student(self, name):
        self.student_roster.append(name)

    def remove_student(self, name):
        self.student_roster.remove(name)

    def add_assignment(self, name):
        self.assignment_roster.append(name)
    
    def remove_assignment(self, name):
        self.assignment_roster.remove(name)