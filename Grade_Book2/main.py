from students import Student
from classroom import Classroom

math = Classroom("math")
math.class_schedule("Tuesday", "10am")
math.add_student("Johnathan", 1)
math.add_student("Jessica", 2)
math.add_student("Johnny", 3)
math.get_student_roster()
math.remove_student("Johnathan")

Johnathan = Student("Johnathan", "math")
Johnathan.add_assignment("Python Loops", 95)
Johnathan.add_assignment("Advanced CS", 90)
Johnathan.add_assignment("Python Challenge", 100)
Johnathan.get_assignment_grade("Python Challenge")
Johnathan.assignment_roster()
Johnathan.grade_average()

Andrew = Student("Andrew", "math")
Andrew.add_assignment("Python Loops", 85)
Johnathan.add_assignment("Advanced CS", 97)

Elmer = Student("Elmer", "math")
Elmer.add_assignment("Python Loops", 80)
Johnathan.add_assignment("Advanced CS", 93)

Jessica = Student("Jessica", "math")
Jessica.add_assignment("Python Loops", 88)
Johnathan.add_assignment("Advanced CS", 92)



