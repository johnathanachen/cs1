from students import Student
from classroom import Classroom

math = Classroom("math")
math.add_student("Johnathan", 1)
math.add_student("Jessica", 2)
math.get_student_roster()

Johnathan = Student("Johnathan", 1)
Johnathan.add_assignment("Python Loops", None)
Johnathan.add_assignment("Advanced CS", 90)
Johnathan.add_assignment("Python Challenge", 100)
Johnathan.get_assignment_grade("Python Challenge")
Johnathan.assignment_roster()
Johnathan.grade_average()