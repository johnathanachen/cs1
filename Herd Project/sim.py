import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):
    def __init__(self, population_size, vacc_percentage, virus_name,
                mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = None
        self.newly_infected = []
        self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        infected_count = 0
        person_id = 1
        print("worked")
        while len(population) != self.population_size:
            if infected_count !=  initial_infected:
                population.append(Person(person_id, is_vaccinated=False, infected=True))
                person_id += 1
                infected_count += 1
                pass              
            else:
                pass 

        print(infected_count)
        print(population)
        return population

def start_this():
    pop_size = 10
    vacc_percentage = 0.90              
    virus_name = "Ebola"
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 10

    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                                basic_repro_num, initial_infected)
start_this()