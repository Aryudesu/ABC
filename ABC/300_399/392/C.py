N = int(input())
P = [int(l) for l in input().split()]
Q = [int(l) for l in input().split()]
graph = dict()
for i in range(N):
    graph[Q[i]] = Q[P[i]-1]
result = []
for i in range(N):
    result.append(graph[i + 1])
print(*result)
