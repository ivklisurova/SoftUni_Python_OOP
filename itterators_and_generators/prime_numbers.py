def get_primes(a):
    for i in a:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                yield i


print(list(get_primes([2,2,2,2, 4, 3, 5, 6, 9, 1, 0])))