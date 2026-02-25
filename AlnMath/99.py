from collections import defaultdict

N = int(input())
graph = defaultdict(list)
for n in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
start = None
for i in range(N):
    if len(graph[i]) == 1:
        start = i
        break
print(start)
