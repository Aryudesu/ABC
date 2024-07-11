def calc(N, T, A):
    H = [0 for n in range(N)]
    W = [0 for n in range(N)]
    D = 0
    U = 0
    for idx in range(T):
        n = A[idx] - 1
        h = n // N
        w = n % N
        H[h] += 1
        if H[h] == N:
            return idx + 1
        W[w] += 1
        if W[w] == N:
            return idx + 1
        if (h == w):
            D += 1
            if D == N:
                return idx + 1
        if (h + w == N - 1):
            U += 1
            if U == N:
                return idx + 1
    return -1


N, T = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print(calc(N, T, A))
