import pytest
from Students import Student

def setup_for_test():
    student = Student("Johnathan", 1)
    return student 

def test_setup():
    student = setup_for_test()
    assert student.name == "Johnathan"
    assert student.student_ID == 1
    assert student.grade_average == None
    assert len(student.assignments) == 0

def test_add_assignment():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    assert student.assignments["python101"] == 100

def test_delete_assignment():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    student.add_assignment("cs quiz", 100)
    student.delete_assignment('python101')
    assert len(student.assignments) == 1 