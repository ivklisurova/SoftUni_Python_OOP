from itertools import permutations


def possible_permutations(l):
    a = list(permutations(l))
    for i in a:
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]

# for n in possible_permutations([1, 2, 3]):
#     print(n)
