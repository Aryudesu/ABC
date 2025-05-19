from collections import defaultdict

from atcoder.dsu import DSU

N, M = [int(l) for l in input().split()]
graph = defaultdict(list)
dsu = DSU(N)
for m in range(M):
    A, B = [int(l) - 1 for l in input().split()]
    graph[A].append(B)
    graph[B].append(A)
    dsu.merge(A, B)
if dsu.size(0) != N:
    print("No")
else:
    result = "Yes"
    for i in range(N):
        if len(graph[i]) != 2:
            result = "No"
            break
    print(result)
