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


N = 10000
count = 0
keys = []
result = dict()
primes = set(calc(N))
for i in range(1000, 10000):
    if i in primes:
        i_str = str(i)
        a, b = int(i_str[:2]), int(i_str[2:])
        if a in primes and b in primes:
            tmp = result.get(a, [])
            if len(tmp) == 0:
                keys.append(a)
            tmp.append(i)
            result[a] = tmp
            count += 1
for key in keys:
    print(*result[key])
print(count, "個")
