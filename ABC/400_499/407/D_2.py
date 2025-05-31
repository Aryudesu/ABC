from collections import defaultdict
from itertools import product


def partition(H: int, W: int, A: list[list[int]]) -> list[list]:
    result1 = []
    result2 = []
    for h in range(H):
        for w in range(W):
            if h % 2 == w % 2:
                result1.append(A[h][w])
            else:
                result2.append(A[h][w])
    return [result1, result2]


def calcXOR(data: list):
    result = defaultdict(list)
    for bits in product([0, 1], repeat = len(data)):
        tmp = None
        count = 0
        for bit, x in zip(bits, data):
            if bit == 1:
                if tmp is None:
                    tmp = x
                else:
                    tmp ^= x
                count += 1
        if tmp is not None:
            result[count].append(tmp)
    return result

def calc(adata: defaultdict, bdata: defaultdict):
    result = 0
    for k in adata:
        adata_k = adata[k]
        bdata_k = bdata[k]
        for a in adata_k:
            for b in bdata_k:
                result = max(result, a^b)
    return result

H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
r1, r2 = partition(H, W, A)
r3, r4 = calcXOR(r1), calcXOR(r2)
print(calc(r3, r4))
