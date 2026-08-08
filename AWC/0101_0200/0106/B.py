from fractions import Fraction

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    if H[u-1] > H[v-1]:
        graph[u-1].append(v-1)
    elif H[u-1] < H[v-1]:
        graph[v-1].append(u-1)
S = []
if K >= 1:
    S = list(map(int, input().split()))
damF = [False] * N
for s in S:
    damF[s-1] = True

result = []
Hidx = []
for idx in range(N):
    Hidx.append((H[idx], idx))
Hidx.sort(reverse=True)
for idx in range(N):
    result.append(W[idx])
for h, idx in Hidx:
    if damF[idx] or len(graph[idx]) == 0:
        continue
    nowNum = result[idx]
    result[idx] = 0
    nextNum = nowNum / len(graph[idx])
    for nextNode in graph[idx]:
        result[nextNode] = result[nextNode] + nextNum
print(*result)
