def pow_ary(a, b):
    if b == 0:
        return 1, 1
    if b > 0:
        return a ** b, 1
    return 1, a ** b

def frac(n):
    if n == 0:
        return 1
    return n * frac(n - 1)

def bernoulli(n):
    if n == 0:
        return 1, 1
    if n == 1:
        return -1, 2
    if n == 2:
        return 1, 6

numer, denom = 1, 1

for k in range(5):
    for l in range(5):
        for m in range(5):
            for n in range(5):
                tmp = (k - 1) + (l - 1) + (m - 1) + n
