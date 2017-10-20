from pathlib import Path

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        my_file = Path(self.file_name)
        if my_file.is_file():
            open(self.file_name, "a+")
        else:
            open(self.file_name, "w+")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        meta = open(self.file_name, "a+")
        meta.write("Pop size: %s\t Vacc percent: %s\t Virus: %s\t Mortality rate: %s\t Repro num: %s\n" % (pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))

    def log_init(self, infected, vacc, normal):
        initial = open(self.file_name, "a+")
        initial.write("Initial // Infected: %s\t Vaccinated: %s\t Normal: %s\t \n" % (infected, vacc, normal))
    
    def log_initial_infected(self, person_id):
        initial = open(self.file_name, "a+")
        initial.write("ID: %s is initially infected \n" % (person_id))
    
    def log_initial_vaccinated(self, person_id):
        initial = open(self.file_name, "a+")
        initial.write("ID: %s is initially vaccinated \n" % (person_id))
    
    def log_initial_created(self, person_id):
        initial = open(self.file_name, "a+")
        initial.write("ID: %s is initially created \n" % (person_id))

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        interaction = open(self.file_name, "a+")
        interaction.write("ID-1: %s\t ID-2: %s\t Infect: %s\t ID-2 Vacc: %s\t ID-2 Infected: %s\n" % (person1._id, person2._id, did_infect, person2_vacc, person2_sick))

    def log_infected(self, person, random_person):
        log_infected = open(self.file_name, "a+")
        log_infected.write("ID: %s is Infected by %s\n" % (random_person._id, person._id))

    def log_infection_death(self, person):
        log_infection = open(self.file_name, "a+")
        log_infection.write("ID: %s\t died from Infection \n" % (person._id))

    def log_survived(self, random, person):
        log_survived = open(self.file_name, "a+")
        log_survived.write("ID: %s\t survived the Infection from ID: %s\n" % (random._id, person._id))
     
    def log_vaccinated(self, person):
        log_vaccinated = open(self.file_name, "a+")
        log_vaccinated.write("ID: %s is Vaccinated\n" % (person._id))

    def log_time_step(self, time_step_number):
        log_steps = open(self.file_name, "a+")
        log_steps.write("Step: %s\n" % (time_step_number))

    def log_cured(self, time_step_counter):
        log = open(self.file_name, "a+")
        log.write("Population Cured \n")
        log.write('The simulation has ended after %s turns. \n' % (time_step_counter))