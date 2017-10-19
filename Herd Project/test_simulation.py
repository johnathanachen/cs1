import pytest
import random, sys
from simulation import Simulation
from person import Person

def setup_for_test():
    pop_size = 25
    vacc_percentage = 0.90              
    virus_name = "Ebola"
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 10
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    return simulation

def test_setup():
    simulation = setup_for_test()
    assert simulation.population_size == 25
    assert simulation.vacc_percentage == 0.90
    assert simulation.virus_name == "Ebola"
    assert simulation.mortality_rate == 0.70
    assert simulation.basic_repro_num == 0.25
    assert simulation.initial_infected == 10
    assert simulation.population == []

def test_create_population():
    simulation = setup_for_test()
    # simulation._create_population(simulation.initial_infected)
    assert len(simulation.population) == 25

def test_simulation_should_continue():
    simulation = setup_for_test()
    population_size = 25
    population = ["one", "two"]
    assert True

def test_run():
    simulation = setup_for_test()
    assert True

