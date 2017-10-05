import pytest
from Students import Student

def setup_for_test():
    student = Student("Johnathan", 1)

def test_setup():
    student = setup_for_test()
    assert student.name == "Johnathan"
    assert student.student_ID == 1
    assert student.grade_average == None
    assert len(student.assignments) == 0

def test_add_assignment():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    assert student.add_assignment["python101"] == 100

def test_delete_assignemnt():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    studnet.add_assignment("cs quiz", 100)
    student.test_delete_assignemnt('python101')
    assert student.assignments['python101'] == 100