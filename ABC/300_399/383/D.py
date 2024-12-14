def calc_p(N):
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

primes = calc_p(4000000)
N = int(input())
result = 0
for i in range(1, len(primes)):
    for j in range(i):
        if (primes[i] * primes[j]) ** 2 <= N:
            result += 1
        else:
            break
for p in primes:
    if p ** 8 <= N:
        result += 1

print(result)
