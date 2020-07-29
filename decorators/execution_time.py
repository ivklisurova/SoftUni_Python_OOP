import time


def exec_time(function):
    def wrapper(*args):
        beginning = time.perf_counter()
        function(*args)
        end = time.perf_counter()
        return end - beginning
    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
