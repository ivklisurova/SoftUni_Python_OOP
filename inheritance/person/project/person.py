class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

# p = Person('Gosho', 13)
# print(p)
# c = Child('Pepi', 2)
# print(c)