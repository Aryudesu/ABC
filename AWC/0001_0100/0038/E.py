from collections import defaultdict

def stableset(graph: dict[int, list[int]])->int:
    pass

N, M, K = map(int, input().split())
P = list(map(int, input().split()))
graph = defaultdict(list)
for k in range(K):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
# えーDP？やっぱMAXFLOW？　うーん？？？？？？
# なにもできてない　たすけて
