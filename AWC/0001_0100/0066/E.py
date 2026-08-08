COUNTER = 0
SCORE = 0

def dfs(S: int, T: int, node: int, prev: int, graph: list[list[int]], C: list[int], memo: int, score: int):
    if node == T:
        global COUNTER
        global SCORE
        COUNTER += 1
        SCORE += score
        return
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode == prev:
            continue
        b = 1 << nextNode
        if b & memo:
            continue
        dfs(S, T, nextNode, node, graph, C, memo | b, score + C[nextNode])



N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N)]
C = []
for n in range(N):
    C.append(int(input()))
# 1方向ならトポロジカルソートで終わるのに・・・・・・
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dfs(S, T, S-1, -1, graph, C, 1 << (S-1), C[S-1])
print(COUNTER, SCORE)
