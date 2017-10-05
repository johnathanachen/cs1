import pytest
from Classroom import Classroom

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

def test_add_students():
    classroom = setup_for_test()
    classroom.add_students("Johnathan")
    assert classroom.roster[0] == "Johnathan"