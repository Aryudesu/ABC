from collections import defaultdict
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
def mergeTopK(A: list[int], B: list[int], K: int = 20) -> list[int]:
    """配列AとBのマージ結果のうち，上位K個の配列を返却します．"""
    i = j = 0
    n, m = len(A), len(B)
    res = []

    while len(res) < K and (i < n or j < m):
        if j >= m or (i < n and A[i] >= B[j]):
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    return res

# データ作成
def makeData(node: int, graph: dict[int, list[int]], memo: set[int], result: list[list[int]], X: list[int]) -> list[int]:
    nextNodes = graph[node]
    res = [X[node]]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        res = mergeTopK(res, makeData(nextNode, graph, memo, result, X))
        memo.discard(nextNode)
    result[node] = res
    return res

N, Q = map(int, input().split())
X = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
data = [None] * N
memo = {0}
data[0] = makeData(0, graph, memo, data, X)
result = []
for _ in range(Q):
    V, K = map(int, input().split())
    result.append(data[V-1][K-1])
for r in result:
    print(r)
