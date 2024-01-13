def calc(N):
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

primes = set(calc(300000))
Q = int(input())
result = []
for q in range(Q):
    x = int(input())
    result.append("Yes" if x in primes else "No")

for r in result:
    print(r)
