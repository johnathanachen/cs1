class assignments(object):

    def __init__(self, name):
        self.name = name
        with open('./db/students.txt', 'r') as student_db:
            student_names = [line.strip() for line in student_db]
            if self.name in student_names:
                pass
            else:
                print(self.name, "is not in the class")
    
    def get_average(self, average):
        self.average = average
        

