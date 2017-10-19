import pytest
import random, sys
from person import Person
from ebola import Ebola

def setup_for_test():
    person = Person(_id=1, is_vaccinated=True, infected=False)
    person.is_alive = True
    person.mortality_rate = .7
    return person

def test_setup():
    person = setup_for_test()
    assert person._id == 1
    assert person.is_vaccinated == True
    assert person.infected == False
    assert person.mortality_rate == .7

# ============================================================

def test_first_infected():
    person = setup_for_test()
    virus = Ebola("Ebola", 0.70, 0.25)
    assert virus.name == "Ebola"
    assert virus.mortality_rate == 0.7

def test_did_survive_infection():
    person = setup_for_test()
    random_num = .5
    assert person.is_alive == False



    

        # virus = self.first_infected()
        # random_num = random.random()
        # if random_num < virus.mortality_rate:
        #     self.is_alive = False
        # else:
        #     self.is_vaccinated = True
        #     self.infected = None