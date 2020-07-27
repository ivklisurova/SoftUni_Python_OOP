class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.counter = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= 0:
            current_num = self.counter
            self.counter -= 1
            return current_num
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
