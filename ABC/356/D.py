MOD = 998244353

def getBit(n):
    tmp = n
    result = []
    while tmp:
        result.append(tmp & 1)
        tmp >>= 1
    return result

def insertZero(A, N):
    while len(A) < N:
        A.append(0)

def calc(N, M):
    NB = getBit(N)
    MB = getBit(M)
    if N > M:
        insertZero(MB, len(NB))
    else:
        insertZero(NB, len(MB))
    NB.reverse()
    MB.reverse()
    L = len(NB)
    data = [0] * L
    ma = 0
    for i in range(L):
        num = (1 << (L - i - 1))
        if NB[i] == 1:
            for j in range(i + 1, L):
                data[j] = (data[j] + num // 2) % MOD
            ma += num
            data[i] = (data[i] + N - ma + 1) % MOD
    result = 0
    for i in range(L):
        if MB[i] == 1:
            result = (result + data[i]) % MOD
    return result

N, M = [int(l) for l in input().split()]
print(calc(N, M))
