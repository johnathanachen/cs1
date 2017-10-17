import pytest
from simulation import Simulation

def test_simulation_should_continue():
    population_size = 0 
    population = []
    return False
    population_size = 1 
    return True
    population = ["John"]
    return True

def if_simulation_should_continue_setup():
    return True

def test_run():
    check_continue = if_simulation_should_continue_setup()
    assert check_continue == True