import random
# TODO: Import the virus clase

class Person(object):
    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected
        self.did_die_from_infection = False

    def __repr__(self):
        return "<id:%s | infected:%s | alive:%s | vaccinated: %s>" % (self._id, self.infected, self.is_alive, self.is_vaccinated)

    def did_survive_infection():
        if self.is_alive == False:
            self.did_die_from_infection = True
            return False
        elif self.is_alive == True:
            self.did_die_from_infection =  False
            self.is_vaccinated = True
            self.infected = None
            return True


