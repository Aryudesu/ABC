N, M = [int(l) for l in input().split()]
C = [l for l in input().split()]
D = [l for l in input().split()]
P = [int(l) for l in input().split()]
data = dict()
for m in range(M):
    data[D[m]] = P[m + 1]
result = 0
for i in range(N):
    result += data.get(C[i], P[0])
print(result)
