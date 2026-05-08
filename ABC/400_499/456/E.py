from atcoder.scc import SCCGraph

def calc()->bool:
    N, M = map(int, input().split())
    graph = [{n} for n in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].add(v-1)
        graph[v-1].add(u-1)

    W = int(input())
    scc = SCCGraph(N * W)
    S = [input() for _ in range(N)]
    for w in range(W):
        for n in range(N):
            if S[n][w] != "o":
                continue
            for nextNode in graph[n]:
                if S[nextNode][(w + 1) % W] != "o":
                    continue
                scc.add_edge(n + N * w, nextNode + N * ((w + 1) % W))
    data = scc.scc()
    for dat in data:
        if len(dat) > 1:
            return True
    return False



result = []
T = int(input())
for _ in range(T):
    result.append("Yes" if calc() else "No")

for r in result:
    print(r)
