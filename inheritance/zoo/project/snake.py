class Animal:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)


class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)

