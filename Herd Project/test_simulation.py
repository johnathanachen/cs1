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
    population = []
    infected_count = 0
    person_id = 1
    while len(population) != simulation.population_size:
        if infected_count != simulation.initial_infected:
            population.append(Person(person_id, is_vaccinated=False, infected=True))
            person_id += 1
            infected_count += 1              
        else:
            rand_num = random.randint(0,1)
            if rand_num < simulation.vacc_percentage:
                population.append(Person(person_id, is_vaccinated=True, infected=False))
                person_id += 1
            elif rand_num > simulation.vacc_percentage:
                population.append(Person(person_id, is_vaccinated=False, infected=False))
                person_id += 1
    assert len(population) == 25

# def test_simulation_should_continue():
#     population_size = 0 
#     population = []
#     return False
#     population_size = 1 
#     return True
#     population = ["John"]
#     return True

# def if_simulation_should_continue_setup():
#     return True

# def test_run():
#     check_continue = if_simulation_should_continue_setup()
#     assert check_continue == True