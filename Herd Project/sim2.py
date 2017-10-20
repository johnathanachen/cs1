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
        self.vaccinated = []
        self.grave_yard = []
        self.time_step_counter = 0
        self.person_id = 0
        self.total_infected = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, population_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        log = Logger(self.file_name)
        log.write_metadata(pop_size=population_size, vacc_percentage=vacc_percentage, virus_name=virus_name, mortality_rate=mortality_rate, basic_repro_num=basic_repro_num)
        self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        while len(self.population) != self.population_size:
            if self.total_infected !=  self.initial_infected:
                self.population.append(Person(self.person_id, is_vaccinated=False, infected=True))
                log = Logger(self.file_name)
                log.log_initial_infected(self.person_id)
                self.person_id += 1
                self.total_infected += 1              
            else:
                rand_num = random.randint(0,1)
                if rand_num < self.vacc_percentage:
                    self.population.append(Person(self.person_id, is_vaccinated=True, infected=False))
                    self.person_id += 1
                elif rand_num > self.vacc_percentage:
                    self.population.append(Person(self.person_id, is_vaccinated=False, infected=False))
                    self.person_id += 1
        self.run()

    def _simulation_should_continue(self):
        if len(self.grave_yard) == len(self.population):
            print("all died")
            return False
        else:
            for i in self.population:
                if i.infected == True and i.is_alive == True:
                    print("keep going")
                    return True
                elif i.infected == False and i.is_alive == True:
                    print("all cured")
                    return False 

    def run(self):
        if self._simulation_should_continue() == True:
            self.time_step_counter += 1
            self.time_step()
        elif self._simulation_should_continue() == False:
            print('The simulation has ended after %s turns.' % (self.time_step_counter))

    def time_step(self):
        log = Logger(self.file_name)
        interaction_counter = 0
        # Find 2 people that are alive
        for i in range(10000):
            for person in self.population:
                random_person = random.choice(self.population)
                if random_person.is_alive == True and person.is_alive == True:
                    self.interaction(person, random_person)
                    interaction_counter += 1
                elif random_person.is_alive == False:
                    self.time_step()
        log.log_time_step(interaction_counter)

    def interaction(self, person, random_person):
        log = Logger(self.file_name)
        did_infect = None
        random_vaccinated = None
        if random_person.infected == False and random_person.is_vaccinated == False and person.infected == True:
            random_num = random.random()
            if random_num < self.basic_repro_num:
                did_infect = True
                log.log_infected(person, random_person)
                random_person.infected = True
                self.infection_death()
            else:
                did_infect = False
                # person is vaccinated if person didn't get infected
                random_person.is_vaccinated = True
                log.log_vaccinated(person)
                self.run()
    
    def infection_death(self):
        log = Logger(self.file_name)
        random_num = random.random()
        for person in self.population:
            if random_num > self.mortality_rate:
                person.is_alive = False
                person.is_vaccinated = False
                log.log_infection_death(person)
                self.grave_yard()
            else:
                person.is_vaccinated = True
                person.is_alive = True
                log.log_survived(person)
                self.run()
    
    def grave_yard(self):
        for person in self.population:
            if person.is_alive == False and person not in self.grave_yard:
                self.grave_yard.append(person)
                self.run()
            else:
                self.run()

        print(self.grave_yard)

def start_this():
    pop_size = 50
    vacc_percentage = 0.90              
    virus_name = "Ebola"
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 10

    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)

start_this()