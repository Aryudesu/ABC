import sys
sys.setrecursionlimit(3*10**5)

N, M = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
person = [False] * (N+1)
graph = dict()
for idx in range(N-1):
    p_ = P[idx]
    tmp = graph.get(p_, [])
    tmp.append(idx + 2)
    graph[p_] = tmp
data = dict()
for m in range(M):
    x, y = [int(l) for l in input().split()]
    tmp = data.get(x, 0)
    if tmp < y:
        data[x] = y


def calc(node, p):
    h = data.get(node, -1)
    if h >= 0 or p >= 0:
        person[node] = True
    hoken = h if h > p else p
    tmp = graph.get(node, [])
    for t in tmp:
        calc(t, hoken - 1)


calc(1, -1)
result = 0
for pr in person:
    if pr:
        result += 1
print(result)
