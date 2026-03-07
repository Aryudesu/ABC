Q = int(input())
result = []
for _ in range(Q):
    N = int(input())
    graph = defaultdict(list)
    for n in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    result.append(calc(N, graph))
for r in result:
    print(r+1)
