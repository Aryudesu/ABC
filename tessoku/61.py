from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(str(b))
    graph[b].append(str(a))
for i in range(1, N + 1):
    print(f"{i}:", "{", end="")
    print(", ".join(graph[i]), end="")
    print("}")
