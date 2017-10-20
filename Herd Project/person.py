import random
from ebola import Ebola

class Person(object):
    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def __repr__(self):
        return "<alive:%s | vaccinated: %s>" % (self.is_alive, self.is_vaccinated)

    def first_infected(self):
        if self.infected == True:
            self.infection = Ebola("Ebola", 0.70, 0.25)
            self.did_survive_infection()
        else:
            self.infection == None
        
        return self.infection
        
    def did_survive_infection(self):
        virus = self.infection
        random_num = random.random()
        if random_num < virus.mortality_rate:
            self.is_alive = False
        else:
            self.is_vaccinated = True
            self.infected = None
           

# x = Person(1,True,True)
# x.first_infected()