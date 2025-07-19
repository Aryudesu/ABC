def calc_prime(N):
    result = [True] * (N + 1)
    primes = [2]
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.append(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes

L, R = [int(l) for l in input().split()]
primes = calc_prime(int(R**0.5))
data = [0] * (R - L + 1)
result = 0
for p in primes:
    for n in range((L//p + 1) * p, R + 1, p):
        data[n - (L + 1)] = 1
        y = n
        while y % p == 0:y //= p
        if y==1:
            result += 1
for d in data:
    if d == 0:
        result += 1
print(result)
