class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.indexes = len(self.dictionary)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.indexes:
            current_element = self.dictionary[self.current_index]
            self.current_index += 1
            return current_element
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
