# from polymorphism_and_magic_methods.wild_farm.project.animals.animal import Mammal
# from polymorphism_and_magic_methods.wild_farm.project.food import Meat, Vegetable, Fruit, Seed

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += food.quantity * 1.0
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


# d = Dog('Doggy', 15, 'sofia')
# v = Vegetable(4)
# print(d.make_sound())
# print(d.feed(v))
# print(d)

# t = Tiger('Tiggy', 100, 'Jungle')
# m = Meat(4)
# t.feed(m)
# print(t)
