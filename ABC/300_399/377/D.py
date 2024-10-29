N, M = [int(l) for l in input().split()]
data = [0] * M
imos = []
data = dict()
for n in range(N):
    L, R = [int(l) - 1 for l in input().split()]
    data[L] = min([data.get(L, M + 1), R])
