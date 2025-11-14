from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def calc(graph: dict[int, list[int]], node: int, result: list[int]) -> int:
    res = 0
    for next in graph[node]:
        res += calc(graph, next, result)
    result[node] = res
    return res + 1

N = int(input())
A = list(map(int, input().split()))
graph = defaultdict(list)
result = [0] * N
for i in range(N-1):
    graph[A[i]-1].append(i+1)
calc(graph, 0, result)
print(*result)
