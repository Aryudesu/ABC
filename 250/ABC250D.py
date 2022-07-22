primes = []
Eratos = [True] * (10**6)
Eratos[0] = False
Eratos[1] = False
for idx in range(2, 10**6):
    if Eratos[idx]:
        primes.append(idx)
        for idx2 in range(idx, 10**6, idx):
            Eratos[idx2] = False

N = int(input())
count = 0
for idx in range(78497):
    for idx2 in range(idx + 1, 78498):
        d = primes[idx] * primes[idx2] * primes[idx2] * primes[idx2]
        if d <= N:
            count += 1
        else:
            break
print(count)
