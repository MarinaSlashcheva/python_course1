def euclid(n, m):
    if n >= m:
        if n % m == 0:
            return m
        else:
            n = n % m
            return euclid(n, m)
    elif m > n:
        if m % n == 0:
            return n
        else:
            m = m % n
            return euclid(n, m)
a, b = [int(i) for i in input().split()]
print(euclid(a, b))