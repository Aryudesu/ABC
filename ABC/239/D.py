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


def calc(A, B, C, D):
    prime = calc_prime(1000)
    for a in range(A, B + 1):
        Aoki = False
        for b in range(C, D + 1):
            if (a + b) in prime:
                Aoki = True
                break
        if not Aoki:
            return "Takahashi"
    return "Aoki"


A, B, C, D = [int(l) for l in input().split()]
print(calc(A, B, C, D))
