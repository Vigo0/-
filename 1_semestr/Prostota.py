def pr(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

print(pr(16))
