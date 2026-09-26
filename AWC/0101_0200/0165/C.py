N = int(input())
U = []
U.append(int(input()))
P = [-1]
for n in range(N-1):
    p, u = map(int, input().split())
    U.append(u)
    P.append(p-1)

INF = 10 ** 18
data = [INF] * N
for pIdx in range(N-1, 0, -1):
    u = min(U[pIdx], data[pIdx])
    data[pIdx] = u
    nextPidx = P[pIdx]
    data[nextPidx] = min(data[nextPidx], u)
if data[0] == 0 or U[0] == 0:
    print(-1)
    exit(0)
data[0] = 1
print(sum(data))
