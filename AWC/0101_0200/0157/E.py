from atcoder.scc import SCCGraph
N, M = map(int, input().split())
W = list(map(int, input().split()))
T = list(map(int, input().split()))
data = [max(0, t - w) for t, w in zip(T, W)]
selfLoop = set()
graph = SCCGraph(N)
for m in range(M):
    u, v = map(int, input().split())
    if u == v:
        selfLoop.add(u-1)
        continue
    graph.add_edge(u-1, v-1)
scc = graph.scc()
result = 0
isOk = True
for s in scc:
    if len(s) <= 1:
        node = s[0]
        if data[node] > 0 and node not in selfLoop:
            isOk = False
            break
        else:
            result += data[node]
        continue
    res = 0
    for node in s:
        res = max(res, data[node])
    result += res
print(result if isOk else -1)
