class Animal:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)

# b = Bear('Yogi')
# print(b.get_name)
