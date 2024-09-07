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


N = 100000
primes = calc(N)
p_set = set(primes)
memo = []
num = 1
for p in primes:
    memo.append(p)
    num *= p
    if not num + 1 in p_set:
        print(num + 1)
        print(memo)
        break
