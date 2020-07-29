def even_parameters(function):
    def wrapper(*args, **kwargs):
        is_even = True
        for i in args:
            if not isinstance(i, int):
                is_even = False
                break
            elif i % 2 != 0:
                is_even = False
                break
        if not is_even:
            return 'Please use only even numbers!'
        return function(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
