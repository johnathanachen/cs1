from students import Student
from classroom import Classroom

math = Classroom("math")
math.class_schedule("Tuesday", "10am")
math.add_student("Johnathan", 1)
math.add_student("Jessica", 2)
math.add_student("Johnny", 3)
math.get_student_roster()
math.remove_student("Johnathan")

Johnathan = Student("Johnathan", 1)
Johnathan.add_assignment("Python Loops", 95)
Johnathan.add_assignment("Advanced CS", 90)
Johnathan.add_assignment("Python Challenge", 100)
Johnathan.get_assignment_grade("Python Challenge")
Johnathan.assignment_roster()
Johnathan.grade_average()