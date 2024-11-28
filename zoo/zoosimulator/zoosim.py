from .animals import Elephant, Giraffe, Monkey

class Zoo:
    #When zoo class is initialised 5 of each animal are generated
    def __init__(self):
        self.current_time = 0
        self.animals = {
            'elephants': [Elephant() for _ in range(5)],
            'monkeys': [Monkey() for _ in range(5)],
            'giraffes': [Giraffe() for _ in range(5)]
        }

    def __str__(self):
        return f'Hours Passed: {self.current_time} Animals: {self.animals['elephants'][0]} {self.animals['monkeys'][0]} {self.animals['giraffes'][0]}'
    
    #Passing time and feeding check if the instance is alive before changing health value
    def add_hour(self):
        for species in self.animals.keys():
            for animal in self.animals[species]:
                if animal.is_alive():
                    animal.reduce_health()
        self.current_time += 1

    def feed(self):
        for species in self.animals.keys():
            for animal in self.animals[species]:
                if animal.is_alive():
                    animal.increase_health()
    
    def get_zoo_status(self):
        #Returns a dictionary of key value pairs 
            #Key being type of animal and value being an array of tuples
            #Tuple for each animal describing it's status 
        status = {
            'monkeys': [(monkey.name, monkey.health, monkey.is_alive()) for monkey in self.animals['monkeys']],
            'giraffes': [(giraffe.name, giraffe.health, giraffe.is_alive()) for giraffe in self.animals['giraffes']],
            'elephants': [(elephant.name, elephant.health, elephant.is_alive()) for elephant in self.animals['elephants']],
        }
        return status