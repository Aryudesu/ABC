N = int(input())
A = list(map(int, input().split()))
P = [-1] + list(map(int, input().split()))
B = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for node in range(1, N):
    parent = P[node]-1
    graph[parent].append(node)
data = [0] * N
nodes = {0}
data[0] = A[0]
while nodes:
    node = nodes.pop()
    for nextNode in graph[node]:
        data[nextNode] = data[node] + A[nextNode]
        nodes.add(nextNode)
result = 0
for i in range(1, N):
    result += data[i] * B[i]
print(result)
