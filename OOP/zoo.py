class Animal(object):
    def __init__(self, name):
        self.name = name
        self.favoriteFood = favoriteFood

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

tiger = Tiger("Johnny")
tiger.eat("meat")
tiger.sleep()



bear = Bear("Johnny")
bear.eat("fish")
bear.sleep()
