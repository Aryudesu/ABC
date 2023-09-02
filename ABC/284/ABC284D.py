M = 10**7
primes = []
Eratos = [True] * (M)
Eratos[0] = False
Eratos[1] = False
for idx in range(2, M):
    if Eratos[idx]:
        primes.append(idx)
        for idx2 in range(idx, M, idx):
            Eratos[idx2] = False
T = int(input())
result = []
for t in range(T):
    N = int(input())
    q = None
    for p in primes:
        if N % (p*p) == 0:
            result.append([p, N // (p*p)])
            break
        elif N % p == 0:
            qq = N // p
            q_ = int(qq ** 0.5)
            if q_ * q_ == qq:
                q = q_
                result.append([q, p])
            elif (q_ + 1) ** 2 == qq:
                q = q_ + 1
                result.append([q, p])
            elif (q_ - 1) ** 2 == qq:
                q = q_ - 1
                result.append([q, p])
            break
    if t + 1 != len(result):
        raise Exception()
for r in result:
    print(*r)
