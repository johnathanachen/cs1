class Classroom(object):
    def __init__(self, name):
        self.name = name
        self.roster = []

    def class_schedule(self, date, time):
        self.class_date = date
        self.class_time = time

    def add_students(self, name):
        self.roster.append(name)