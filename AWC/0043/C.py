from collections import defaultdict
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
INF = 10**18

def calc(node: int, graph:dict[int, list[int]], W: list[int], unBalance: list[int])->int:
    nextNodes = graph[node]
    if len(nextNodes) == 0:
        unBalance[node] = 0
        return W[node]
    minNum = INF
    maxNum = -INF
    sumNum = 0
    for nextNode in nextNodes:
        res = calc(nextNode, graph, W, unBalance)
        minNum = min(minNum, res)
        maxNum = max(maxNum, res)
        sumNum += res
    if len(nextNodes) >= 2:
        unBalance[node] = maxNum - minNum
    else:
        unBalance[node] = 0
    return sumNum


N = int(input())
P = list(map(int, input().split()))
W = list(map(int, input().split()))
graph = defaultdict(list)
unBalance = [-INF] * N
for i in range(N-1):
    graph[P[i]-1].append(i+1)
calc(0, graph, W, unBalance)
print(max(unBalance))

