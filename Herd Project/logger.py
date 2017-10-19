from pathlib import Path

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.tab = '\t+'
        self.new_line = "\n"
        my_file = Path(self.file_name)
        if my_file.is_file():
            open(self.file_name, "a+")
        else:
            open(self.file_name, "w+")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        meta = open(self.file_name, "a+")
        metadata = [pop_size, self.tab, vacc_percentage, self.tab, virus_name, self.tab, mortality_rate, self.tab, basic_repro_num, self.new_line]
        for i in metadata:
            meta.write(str(i))

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        pass


    def log_infection_survival(self, person, did_die_from_infection):
        log_infection = open(self.file_name, "a+")
        infection_data = [person, tab, did_die_from_infection, new_line]
        for i in infection_data:
            log_infection.write(str(i))

    def log_time_step(self, time_step_number):
        log_steps = open(self.file_name, "a+")
        log_steps.write(str(time_step_number) + self.new_line)