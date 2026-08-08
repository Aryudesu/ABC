from collections import defaultdict

N, Q = map(int, input().split())
V = list(map(int, input().split()))
P = [-1] + [int(l) - 1 for l in input().split()]
graph = defaultdict(list)
for i in range(N):
    p = P[i]
    # pの子がiになる
    graph[p].append(i)
data = [0] * N
nodes = {(0, V[0])}
data[0] = V[0]
while nodes:
    nextNodes = set()
    for parent, v in nodes:
        for child in graph[parent]:
            newV = v + V[child]
            data[child] = newV
            nextNodes.add((child, newV))
    nodes = nextNodes
result = []
for _ in range(Q):
    X = int(input())
    result.append(data[X-1])
for r in result:
    print(r)
