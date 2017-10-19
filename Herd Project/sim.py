import random, sys
random.seed(44)
from person import Person
from logger import Logger

class Simulation(object):
    def __init__(self, population_size, vacc_percentage, virus_name,
                mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
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
        Log = Logger(self.file_name)
        Log.write_metadata(pop_size=population_size, vacc_percentage=vacc_percentage, virus_name=virus_name, mortality_rate=mortality_rate, basic_repro_num=basic_repro_num)

    def _create_population(self, initial_infected):
        population = []
        infected_count = 0
        person_id = 1
        while len(population) != self.population_size:
            if infected_count !=  initial_infected:
                population.append(Person(person_id, is_vaccinated=False, infected=True))
                person_id += 1
                infected_count += 1              
            else:
                rand_num = random.randint(0,1)
                if rand_num < self.vacc_percentage:
                    population.append(Person(person_id, is_vaccinated=True, infected=False))
                    person_id += 1
                elif rand_num > self.vacc_percentage:
                    population.append(Person(person_id, is_vaccinated=False, infected=False))
                    person_id += 1

        self.population = population
  

    def time_step(self):
        interaction_counter = 0
        infected_list = []

        for select_person in self.population:
            if select_person.infected == True:
                infected_list.append(select_person)

        for select_person in self.population:
            random_person = random.choice(self.population)
            if random_person.is_alive == True and select_person.is_alive == True:
                self.interaction(select_person, random_person)
                interaction_counter += 1

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.infected == False and random_person.is_vaccinated == False:
            random_num = random.random()
            if random_num < self.basic_repro_num:
                self.newly_infected.append(random_person._id)

    def _infect_newly_infected(self):
        for person_id in self.newly_infected:
            for person in self.population:
                if person._id == person_id:
                    person.infected = True
 
        self.newly_infected = []


        
def start_this():
    pop_size = 50
    vacc_percentage = 0.90              
    virus_name = "Ebola"
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 10

    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    
    simulation.time_step()
    simulation._infect_newly_infected()
start_this()