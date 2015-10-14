def euclid(n, m):
    if n >= m:
        if n % m == 0:
            return m
        else:
            n = n % m
            return euclid(n, m)
    else:
            return euclid(m, n % m)
a, b = [int(i) for i in input().split()]
print(euclid(a, b))