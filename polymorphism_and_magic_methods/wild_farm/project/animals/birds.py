# from polymorphism_and_magic_methods.wild_farm.project.animals.animal import Bird
# from polymorphism_and_magic_methods.wild_farm.project.food import Meat, Vegetable, Fruit, Seed

from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable) or isinstance(food, Fruit) or isinstance(food, Seed):
            self.weight += food.quantity * 0.35
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
