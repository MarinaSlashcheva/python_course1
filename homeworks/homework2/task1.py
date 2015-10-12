def combinations(n, k):
    if k > n:
        return 0
    elif n == k or k == 0:
        return 1
    else:
        return combinations(n-1, k-1) + combinations(n-1, k)
n, k = [int(i) for i in input(). split()]
print(combinations(n, k))
