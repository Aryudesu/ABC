import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

def dfs(graph: list[int], node: int, memo: list[bool], result: list[int]):
    if memo[node]:
        result.append(node)
        return
    memo[node] = True
    dfs(graph, graph[node], memo, result)
    if memo[result[0]]:
        result.append(node)
    memo[node] = False
    return

def calc(start: int, Q: int, graph: list[int], loop: list[int])->int:
    loopSet = set(loop)
    now = start
    for q in range(Q):
        now = graph[now]
        if now in loopSet:
            # 残り移動回数
            move = Q - (q + 1)
            nowIdx = loop.index(now)
            return loop[(nowIdx + move) % 2]
    return now


N, S, Q = map(int, input().split())
X = list(map(int, input().split()))
data = [(X[n], n) for n in range(N)]
data.sort()
graph = [None] * N
for idx in range(N):
    x, n = data[idx]
    if idx == 0:
        graph[data[idx][1]] = data[1][1]
        continue
    elif idx == N-1:
        graph[data[idx][1]] = data[idx-1][1]
        continue
    l = data[idx][0] - data[idx-1][0]
    r = data[idx+1][0] - data[idx][0]
    if l > r:
        graph[data[idx][1]] = data[idx+1][1]
    elif l < r:
        graph[data[idx][1]] = data[idx-1][1]
    else:
        nl = data[idx-1][1]
        nr = data[idx+1][1]
        graph[data[idx][1]] = min(nl, nr)

memo = [False] * N
loop = []
dfs(graph, S-1, memo, loop)
loop.pop()
print(calc(S-1, Q, graph, loop) + 1)
