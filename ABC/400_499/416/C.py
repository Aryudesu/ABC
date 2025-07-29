from itertools import product

def makeData(N, K, X, S):
    data = []
    for dat in product([i for i in range(N)], repeat=K):
        s = ""
        for idx in dat:
            s += S[idx]
        data.append(s)
    data.sort()
    # print(data)
    return data[X-1]


N, K, X = [int(l) for l in input().split()]
S = [input() for _ in range(N)]
print(makeData(N, K, X, S))
