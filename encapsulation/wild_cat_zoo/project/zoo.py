class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget < price:
            return f'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return f'Not enough space for animal'
        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return f'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        w = [w for w in self.workers if w.name == worker_name]
        if not w:
            return f'There is no {worker_name} in the zoo'
        self.workers.remove(w[0])
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        sal = [s.salary for s in self.workers]
        monthly_salaries = sum(sal)
        if monthly_salaries > self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= monthly_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        tend_need = 0
        for a in self.animals:
            tend_need += a.get_needs()

        if self.__budget < tend_need:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= tend_need
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        l = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        t = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        c = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(l)} Lions:\n'
        result += '\n'.join([x.__repr__() for x in l]) + '\n'
        result += f'----- {len(t)} Tigers:\n'
        result += '\n'.join([x.__repr__() for x in t]) + '\n'
        result += f'----- {len(c)} Cheetahs:\n'
        result += '\n'.join([x.__repr__() for x in c])
        return result

    def workers_status(self):
        k = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        c = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        v = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(k)} Keepers:\n'
        result += '\n'.join([x.__repr__() for x in k]) + '\n'
        result += f'----- {len(c)} Caretakers:\n'
        result += '\n'.join([x.__repr__() for x in c]) + '\n'
        result += f'----- {len(v)} Vets:\n'
        result += '\n'.join([x.__repr__() for x in v])
        return result


