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

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        interaction = open(self.file_name, "a+")
        interaction.write("ID-1: %s\t ID-2: %s\t Infect: %s\t ID-2 Vacc: %s\t ID-2 Infected: %s\n" % (person1._id, person2._id, did_infect, person2_vacc, person2_sick))


    def log_infection_survival(self, person, did_die_from_infection):
        log_infection = open(self.file_name, "a+")
        log_infection.write("ID: %s\t Death from Infection: %s\t" % (person, did_die_from_infection))


    def log_time_step(self, time_step_number):
        log_steps = open(self.file_name, "a+")
        log_steps.write("Step: %s\n" % (time_step_number))
