def getNum(A):
    result = 0
    for a in A:
        n = int(a)
        result |= 1 << (n-1)
    return result

N, M, K = [int(l) for l in input().split()]
data = [True] * (2 ** N)
for m in range(M):
    C, *A, R = [l for l in input().split()]
    num = getNum(A)
    if R == 'o':
        for i in range(2 ** N):
            if data[i] and (i & num).bit_count() < K:
                data[i] = False
    else:
        for i in range(2 ** N):
            if data[i] and (i & num).bit_count() >= K:
                data[i] = False
print(data.count(True))
