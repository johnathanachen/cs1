import random, sys
random.seed(42)
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
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = None
        self.newly_infected = []

    def _create_population(self, initial_infected):
        population = []
        infected_count = 0
        person_id = 1
        while len(population) != self.population_size:
            if infected_count !=  initial_infected:
                self.population.append(Person(person_id, is_vaccinated=False, infected=True))
                person_id += 1
                infected_count += 1              
            else:
                rand_num = random.randint(0,1)
                if rand_num < self.vacc_percentage:
                    self.population.append(Person(person_id, is_vaccinated=True, infected=False))
                    person_id += 1
                elif rand_num > self.vacc_percentage:
                    self.population.append(Person(person_id, is_vaccinated=False, infected=False))
                    person_id += 1

        return population

    def _simulation_should_continue(self):
        if population_size == 0 or len(population) == 0:
            return False
        else: 
            return True

    def run(self):
        time_step_counter = 0
        should_continue = None
        self._simulation_should_continue()
        while should_continue:
            self._simulation_should_continue()
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
        pass

    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person1.is_alive == True
        assert random_person.is_alive == True

        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than basic_repro_num, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Remember to call self.logger.log_interaction() during this method!
        pass

    def _infect_newly_infected(self):
        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!
        pass
  
if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    simulation.run()