class Student(object):
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.grade_average = None
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def delete_assignment(self, assignment_name):
        del self.assignments[assignment_name]


