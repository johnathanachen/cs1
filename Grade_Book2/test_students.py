import pytest
from students import Student

def setup_for_test():
    student = Student("Johnathan", 1)
    return student 

def test_setup():
    student = setup_for_test()
    assert student.name == "Johnathan"
    assert student.student_ID == 1
    assert student.class_grade == int
    assert len(student.assignments) == 0

def test_add_assignment():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    assert student.assignments["python101"] == 100
    student.add_assignment("python challenge", 95)
    assert student.assignments["python challenge"] == 95

def test_get_assignment_grade():
    student = setup_for_test()
    student.add_assignment("Python Challenge", 100)
    student.add_assignment("cs quiz", 95)
    assert student.assignments["Python Challenge"] == 100
    # Needs works

def test_delete_assignment():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    student.add_assignment("cs quiz", 100)
    student.delete_assignment('python101')
    assert len(student.assignments) == 1 

def test_assignment_roster():
    student = setup_for_test()
    student.add_assignment("python101", 100)
    student.add_assignment("cs quiz", 100)
    assert len(student.assignments) == 2
    
def test_grade_average():
    student = setup_for_test()
    student.add_assignment("python101", 95)
    student.add_assignment("cs quiz", 100)
    assert student.class_grade == int