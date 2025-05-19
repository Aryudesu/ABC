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

primes = calc_prime(10000000)
N = int(input())
n = N
result = 0
data = []
for p in primes:
    while True:
        if n % p == 0:
            n = n // p
            data.append(p)
        if n % p != 0:
            break
if n != 1:
    data.append(n)

num = len(data)
result = 0
c = 1
while c < num:
    c *= 2
    result += 1
print(result)
