import pytest
import random, sys
from person import Person

def setup_for_test():
    _id = 1
    is_vaccinated = True
    infected = False
    person = Person(_id, is_vaccinated, infected)
    return person

def test_setup():
    person = setup_for_test()
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == False

def test_did_survive_infection():
    person = setup_for_test()
    person.is_alive = True
    assert person.is_vaccinated == True

    

