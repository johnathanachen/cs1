import random
# TODO: Import the virus clase

class Person(object):
    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infected = infected

    def __repr__(self):
        return "<id:%s infected:%s alive:%s>" % (self._id, self.infected, self.is_alive)

    def did_survive_infection():
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infected = None, return True.  
        pass
