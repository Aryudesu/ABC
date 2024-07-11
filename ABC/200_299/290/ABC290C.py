def calc(K, A):
    if len(A) < K:
        lA = len(A)
        for l in range(lA):
            if A[l] != l:
                return l
        return lA
    for k in range(K):
        if A[k] != k:
            return k
    return K


N, K = [int(l) for l in input().split()]
A = list({int(l) for l in input().split()})
A.sort()
print(calc(K, A))
