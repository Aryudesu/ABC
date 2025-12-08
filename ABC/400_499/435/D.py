import sys
import pypyjit
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

def dfs(node: int, memo: list[bool], graph: list[list[int]]):
    if memo[node]:
        return
    memo[node] = True
    for nextNode in graph[node]:
        if memo[nextNode]:
            continue
        dfs(nextNode, memo, graph)

N, M = map(int, input().split())
fromNode = [[] for _ in range(N+1)]
for m in range(M):
    x, y = map(int, input().split())
    fromNode[y].append(x)

blackAbleList = [False] * (N + 1)

result = []
Q = int(input())
for q in range(Q):
    n, v = map(int, input().split())
    if n == 1:
        dfs(v, blackAbleList, fromNode)
    elif n == 2:
        result.append("Yes" if blackAbleList[v] else "No")
    else:
        raise Exception()
for r in result:
    print(r)
