class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.count:
            self.counter += 1
            current_num = self.num
            self.num += self.step
            return current_num
        raise StopIteration()


numbers = take_skip(0, 10)
for number in numbers:
    print(number)
