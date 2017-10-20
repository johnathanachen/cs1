import random, sys
# random.seed(44)
from person import Person
from logger import Logger

class Simulation(object):
    def __init__(self, population_size, vacc_percentage, virus_name,
                mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = []
        self.vacc_count = 0
        self.death_count = 0
        self.interaction_counter = 0
        self.time_step_counter = 0
        self.person_id = 0
        self.total_infected = 0
        self.current_person = 0
        self.current_random_person = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        log = Logger(self.file_name)
        log.write_metadata(pop_size=population_size, vacc_percentage=vacc_percentage, virus_name=virus_name, mortality_rate=mortality_rate, basic_repro_num=basic_repro_num)
        self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        log = Logger(self.file_name)
        self.init_infected_count = 0
        self.init_vacc_count = 0
        self.init_created_count = 0
        while len(self.population) != self.population_size:
            if self.total_infected !=  self.initial_infected:
                self.population.append(Person(self.person_id, is_vaccinated=False, infected=True))
                log.log_initial_infected(self.person_id)
                self.person_id += 1
                self.init_infected_count += 1
                self.total_infected += 1              
            else:
                rand_num = random.randint(0,1)
                if round(rand_num,2) < self.vacc_percentage:
                    self.population.append(Person(self.person_id, is_vaccinated=True, infected=False))
                    self.person_id += 1
                    self.init_vacc_count += 1
                    log.log_initial_vaccinated(self.person_id)
                elif round(rand_num,2) > self.vacc_percentage:
                    self.population.append(Person(self.person_id, is_vaccinated=False, infected=False))
                    self.person_id += 1
                    self.init_created_count += 1
                    log.log_initial_created(self.person_id)
        log.log_init(self.init_infected_count,self.init_vacc_count,self.init_created_count)
        self.run()

    def _simulation_should_continue(self):
        log = Logger(self.file_name)
        if self.death_count == len(self.population):
            log.log_all_dead(self.time_step_counter)
            print('The simulation has ended after %s turns.' % (self.time_step_counter))            
        elif self.death_count + self.vacc_count == len(self.population):
            log.log_cured(self.time_step_counter)
            print('The simulation has ended after %s turns.' % (self.time_step_counter)) 
        else:
            print("keep going")
            self.time_step()

    def run(self):        
        self.time_step_counter += 1
        self._simulation_should_continue()

    def time_step(self):
        self._infected_person()
        self._random_person()
        self.interaction(self.current_person, self.current_random_person)
        
    def _infected_person(self):
        for person in self.population:
            if person.infected == True and person.is_alive == True and person.is_vaccinated == False: 
                self.current_person = person

    def _random_person(self):
        for random_person in self.population:
            if random_person.infected == False and random_person.is_alive == True and random_person.is_vaccinated == False:
                self.current_random_person = random_person
        
    def interaction(self, person, random_person):
        log = Logger(self.file_name)
        did_infect = None
        random_vaccinated = None
        self.interaction_counter += 1
        log.log_time_step(self.interaction_counter)
        random_num = random.random()
        if random_num < self.basic_repro_num:
            did_infect = True
            log.log_infected(person, random_person)
            random_person.infected = True
            random_num = random.random()
            if random_num > self.mortality_rate:
                random_person.is_alive = False
                random_person.is_vaccinated = None
                log.log_infection_death(random_person)
                self.death_count += 1
                self.run()
            else:
                random_person.is_vaccinated = True
                random_person.is_alive = True
                log.log_survived(random_person, person)
                self.vacc_count += 1
                self.run()
        else:
            did_infect = False
            random_person.is_vaccinated = True
            log.log_vaccinated(person)
            self.vacc_count += 1
            self.run()

def start_this():
    pop_size = 50
    vacc_percentage = 0.90              
    virus_name = "Ebola"
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 5

    simulation = Simulation(population_size=pop_size, vacc_percentage=vacc_percentage, virus_name=virus_name, mortality_rate=mortality_rate, basic_repro_num=basic_repro_num, initial_infected=initial_infected)

start_this()

