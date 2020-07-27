class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.length = len(self.sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            if self.index == self.length:
                self.index = 0
            if self.index < self.length:
                temp = self.sequence[self.index]
                self.index += 1
                self.counter += 1
                return temp
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
