from itertools import product


def calc(N, K, A):
    L = N // 2
    A1 = []
    A2 = []
    for n in range(N):
        if n < L:
            A1.append(A[n])
        else:
            A2.append(A[n])
    data1 = set()
    for dat in product([0, 1], repeat=L):
        tmp = 0
        for l in range(L):
            tmp += A1[l] * dat[l]
        data1.add(tmp)
    for dat in product([0, 1], repeat=N-L):
        tmp = 0
        for l in range(N-L):
            tmp += A2[l] * dat[l]
        if K - tmp in data1:
            return True
    return False



N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
print("Yes" if calc(N, K, A) else "No")
