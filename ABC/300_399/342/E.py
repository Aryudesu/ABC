from heapq import heappop, heappush

N, M = [int(l) for l in input().split()]
MAX = 10**18
graph = dict()
for m in range(M):
    l, d, k, c, a, b = [int(l) for l in input().split()]
    tmp = graph.get(b, [])
    tmp.append([a, l, d, k, c])
    graph[b] = tmp
data = [-MAX] * (N + 1)
Q = []
# 最大の数値が欲しい
for dat in graph.get(N, []):
    a, l, d, k, c = dat
    tmp = l + (k - 1) * d + c
    heappush(Q, (-(tmp - c), a))
    data[a] = tmp - c
while Q:
    d_u, u = heappop(Q)
    if data[u] > -d_u:
        continue
    for a, l, d, k, c in graph.get(u, []):
        tmp = (-d_u - c - l) // d
        if tmp > k - 1:
            continue
        alt = l + tmp * d
        if data[a] < alt:
            data[a] = alt
            heappush(Q, (-alt, a))
for idx in range(1, N):
    d = data[idx]
    if d < 0:
        print("Unreachable")
    else:
        print(d)
