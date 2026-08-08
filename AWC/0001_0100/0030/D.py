import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)


def dfs(depth: int, node: int, graph: int, memo: list[int|None], result: list[int|None])->int:
    # print(depth, result, memo)
    nextNode = graph[node]
    if result[nextNode] is not None:
        result[node] = result[nextNode]
        return result[nextNode]
    if memo[nextNode] is not None:
        res = depth - memo[nextNode] + 1
        result[node] = res
        return res
    memo[node] = depth
    res = dfs(depth + 1, nextNode, graph, memo, result)
    result[node] = res
    return res
    


N = int(input())
T = [int(l) - 1 for l in input().split()]
memo = [None] * N
result = [None] * N
for node in range(N):
    if result[node] is not None:
        continue
    dfs(1, node, T, memo, result)
print(*result)
