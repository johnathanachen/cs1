class Student(object):
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
            self.assignments[assignment_name] = grade
    
    def get_assignment_grade(self, assignment_name):
        self.assignment_name = assignment_name
        print(self.name, "recieved a", self.assignments[assignment_name], "on", self.assignment_name)

    def delete_assignment(self, assignment_name):
        del self.assignments[assignment_name]
    
    def assignment_roster(self):
        print(self.assignments)
    
    def grade_average(self):
        grade_list = self.assignments.values()
        number_of_assignments = len(grade_list)
        total_points = sum(grade_list)
        print(int(total_points/number_of_assignments))
  
  





