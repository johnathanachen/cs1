import pytest
from classroom import Classroom

def setup_for_test():
    classroom = Classroom("Math")
    return classroom 

def test_setup():
    classroom = setup_for_test()
    assert classroom.name == "Math"

def test_class_schedule():
    classroom = setup_for_test()
    classroom.class_schedule("Tuesday", "10am")
    assert classroom.class_date == "Tuesday"
    assert classroom.class_time == "10am"

def test_add_student():
    classroom = setup_for_test()
    classroom.add_student("Johnathan", 1)
    assert classroom.student_roster["Johnathan"] == 1
    classroom.add_student("Jessica", 2)
    assert classroom.student_roster["Jessica"] == 2
    assert len(classroom.student_roster) == 2

def test_remove_student():
    classroom = setup_for_test()
    classroom.add_student("Johnathan", 1)
    classroom.add_student("Jessica", 2)
    classroom.remove_student("Jessica")
    assert len(classroom.student_roster) == 1

def test_get_student_roster():
    classroom = setup_for_test()
    classroom.add_student("Johnathan", 1)
    classroom.add_student("Jessica", 2)
    assert classroom.student_roster == {"Johnathan": 1, "Jessica": 2}

def test_add_assignment():
    classroom = setup_for_test()
    classroom.add_assignment("python hw")
    assert classroom.assignment_roster[0] == "python hw"
    assert len(classroom.assignment_roster) == 1
    classroom.add_assignment("python quiz")
    assert classroom.assignment_roster[1] == "python quiz"
    assert len(classroom.assignment_roster) == 2

def test_remove_assignment():
    classroom = setup_for_test()
    classroom.add_assignment("python hw")
    classroom.add_assignment("python quiz")
    classroom.remove_assignment("python hw")
    assert len(classroom.assignment_roster) == 1