import random

class Animal:
    def __init__(self, name: str, health: float = 100.0):
        self.name = name
        self.health = health

    #String method runs when an object is printed
    def __str__(self):
        return f"{self.name} (Health: {self.health:.2f}%)"
    
    def reduce_health(self):
        damage_percentage = random.uniform(0, 20)
        self.health -= (damage_percentage * self.health) / 100
        self.health = max(0, self.health)

    def increase_health(self):
        feed_percentage = random.uniform(10, 25)
        self.health += (feed_percentage * self.health) / 100
        self.health = min(100, self.health)

    #Overridden in child classes
    def is_alive(self):
        return self.health > 0



class Elephant(Animal):
    def __init__(self):
        super().__init__(name="Elephant")
    
    #Overrides the parent method to set the elephant's ability to walk
    def decrease_health(self):
        super().decrease_health()
        if self.health < 70:
            self.can_walk = False
        else:
            self.can_walk = True

    def is_alive(self):
        if self.health < 70:
            return False  # Elephant dies if health doesn't recover above 70%
        return super().is_alive()

    
class Monkey(Animal):
    def __init__(self):
        super().__init__(name="Monkey")
    
    def is_alive(self):
        return self.health > 30

class Giraffe(Animal):
    def __init__(self):
        super().__init__(name="Giraffe")
    
    def is_alive(self):
        return self.health > 50