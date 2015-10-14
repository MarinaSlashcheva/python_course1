def euclid(n, m):
    if n >= m:
        if n % m == 0:
            return m
        else:
            n = n % m
            return euclid(n, m)
    else:
            return euclid(m, n % m)

def rpfilter(a, *args):
    list_prime = []
    for arg in args:
        prime = euclid(a, arg)
        if prime == 1:
            list_prime.append(arg)
    return list_prime

input_num = [int(i) for i in input().split()]
primes = rpfilter(*input_num)
for num in primes:
    print(num, end=' ')
if len(primes) == 0:
    print(None)
