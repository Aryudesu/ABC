from collections import defaultdict
from heapq import heappop, heappush
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
def addNodes(okNodes: set, nodeData: list, nodeDataSet: set, graph: dict[list[int]], num: int, k):
    if num > k:
        return
    if num in okNodes:
        return
    if num in nodeDataSet:
        okNodes.add(num)
        nodeDataSet.discard(num)
        for nextNode in graph[num]:
            if nextNode in okNodes:
                nodeDataSet.discard(nextNode)
                continue
            if not nextNode in nodeDataSet:
                heappush(nodeData, nextNode)
                nodeDataSet.add(nextNode)
            addNodes(okNodes, nodeData, nodeDataSet, graph, nextNode, k)

N, M = map(int, input().split())
graph = defaultdict(set)
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].add(v-1)
result = []
# 繋がった頂点
okNodes = set()
# 繋げられる頂点
nodeDataSet = set()
nodeDataSet.add(0)
nodeData = [0]
# k = 0から調べる
for k in range(N):
    addNodes(okNodes, nodeData, nodeDataSet, graph, k, k)
    while nodeData:
        num = heappop(nodeData)
        if not num in nodeDataSet:
            continue
        if num > k:
            break
        addNodes(okNodes, nodeData, nodeDataSet, graph, num, k)
    # k以下の頂点全て通過可能であれば
    if len(okNodes) == k + 1:
        result.append(len(nodeDataSet))
    else:
        result.append(-1)
for r in result:
    print(r)
