# from django.db import models
# import random


# class Animal(models.Model):
#     name = models.CharField(max_length=50)
#     health = models.FloatField(default=100.0)  # Health as a percentage (0-100)
#     zoo = models.ForeignKey('Zoo', on_delete=models.CASCADE, related_name='animals')
    
#     def apply_damage(self):
#         damage_percentage = random.uniform(0, 20)  # Random damage between 0 and 20%
#         self.health -= (damage_percentage * self.health) / 100
#         self.health = max(0, self.health)  # Ensure health doesn't go below 0
#         self.save()

#     def feed(self, percentage_increase):
#         increase = (percentage_increase * self.health) / 100
#         self.health += increase
#         self.health = min(100, self.health)  # Cap health at 100
#         self.save()

#     class Meta:
#         abstract = True

# class Monkey(Animal):
#     zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, related_name='monkeys')
#     def is_dead(self):
#         return self.health < 30


# class Giraffe(Animal):
#     zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, related_name='giraffes')
#     def is_dead(self):
#         return self.health < 50


# class Elephant(Animal):
#     zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE, related_name='elephants')
#     def is_dead(self):
#         if self.health < 70:
#             return True  # Elephant is dead if health is under 70%
#         return False


# # Zoo Model
# class Zoo(models.Model):
#     time = models.IntegerField(default=0)  # Time in hours
#     monkeys = models.IntegerField(default=5)
#     giraffes = models.IntegerField(default=5)
#     elephants = models.IntegerField(default=5)

#     def pass_time(self):
#         self.time += 1
#         for animal in self.animals.all():
#             animal.apply_damage()  # Apply damage to each animal every hour
#             if animal.is_dead():
#                 animal.delete()  # Remove dead animals from the zoo
#         self.save()

#     def feed_animals(self):
#         for monkey in self.animals.filter(type='Monkey'):
#             monkey.feed(random.uniform(10, 25))  # Feed monkeys
#         for giraffe in self.animals.filter(type='Giraffe'):
#             giraffe.feed(random.uniform(10, 25))  # Feed giraffes
#         for elephant in self.animals.filter(type='Elephant'):
#             elephant.feed(random.uniform(10, 25))  # Feed elephants
#         self.save()

#     def add_animals(self):
#         # Create 5 of each animal when the zoo is initialized
#         self.animals.bulk_create([
#             Monkey(name='Monkey', zoo=self),
#             Giraffe(name='Giraffe', zoo=self),
#             Elephant(name='Elephant', zoo=self)
#         ])
#         self.save()

#     class Meta:
#         unique_together = ('name', 'animal_type')