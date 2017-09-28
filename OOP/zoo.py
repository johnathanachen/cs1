class Animal(object):
    population = 0
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def populationCount(cls):
        cls.population += 1
        return cls.population
        print(cls.population)
    
    def sleep(self):
        print(self.name , "sleeps for 8 hours")

    def eat(self, food):
        self.food = food
        food = self.food
        print(self.name ,  "eats", food)
        if food == self.favoriteFood:
            print("YUM!", self.name ,  "wants more", food)
        else:
            pass


class Tiger(Animal):
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print(self.name, "sleeps for 8 hours")

    def eat(self, food):
        self.food = food
        favoriteFood = "meat"
        print(self.name,  "eats", food)
        if food == favoriteFood:
            print("YUM!", self.name,  "wants more", food)
        else:
            pass

class Bear(Animal):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name, "hibernates for 4 months")

    def eat(self, food):
        self.food = food
        favoriteFood = "fish"
        print(self.name,  "eats", food)
        if food == favoriteFood:
            print("YUM!", self.name,  "wants more", food)
        else:
            pass

class Unicorn(Animal):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name, "sleeps in a cloud")

    def eat(self, food):
        self.food = food
        favoriteFood = "marshmallows"
        print(self.name,  "eats", food)
        if food == favoriteFood:
            print("YUM!", self.name,  "wants more", food)
        else:
            pass

class Giraffe(Animal):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name, "sleeps for 8 hours")

    def eat(self, food):
        self.food = food
        favoriteFood = "leaves"
        print(self.name,  "eats", food)
        if food == favoriteFood:
            print("YUM!", self.name,  "wants more", food)
        else:
            print("YUCK!", self.name, "spits out", food)

class Bee(Animal):
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(self.name, "never sleeps")

    def eat(self, food):
        self.food = food
        favoriteFood = "pollen"
        print(self.name,  "eats", food)
        if food == favoriteFood:
            print("YUM!", self.name,  "wants more", food)
        else:
            print("YUCK!", self.name, "spits out", food)

class Zookeeper(object):
    def __init__(self, name):
        self.name = name

    def feedAnimals(self, animals, food):
        self.animals = animals
        self.food = food
        population_count = Animal.populationCount()
        print(self.name, "is feeding", self.food, "to", len(self.animals), "of",population_count , "total animals")    
        for i in animals:
            i.populationCount()
            i.eat(self.food)
            i.sleep()