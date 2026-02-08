from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
graph = MFGraph(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.add_edge(a-1, b-1, c)
print(graph.flow(0, N-1))
