from collections import defaultdict

def makeData1(graph: dict, memo: set, node: int, start: int, depth: int, maxMemo: list):
    nextNodes = graph[node]
    maxDepth = 0
    maxNode = -1
    maxNext = -1
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        res1, res2, res3 = makeData1(graph, memo, nextNode, start, depth + 1, maxMemo)
        if maxDepth <= res2:
            if maxNode < res1:
                maxNode = res1
                maxNext = res3
            maxDepth = res2
        memo.discard(nextNode)
    if maxNode == -1:
        maxDepth = depth
        maxNode = start
        maxNext = node
    maxMemo[node] = [maxNode, maxDepth, maxNext]
    return maxNode, maxDepth, maxNext

def makeData2(graph: dict, memo: set, node: int, start: int, depth, maxDepth: int, maxMemo: list):
    nextNodes = graph[node]
    maxNode, maxDepth, maxNext = maxMemo[node]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        if nextNode == maxNext:
            makeData2(graph, memo, nextNode, start, depth + 1, maxDepth - 1, maxMemo)
        else:
            makeData2(graph, memo, nextNode, start, depth + 1, maxDepth + 1, maxMemo)
        memo.discard(nextNode)

N = int(input())
graph = defaultdict(list)
memo = set()
# Fromと最大深度を保存 [From, maxDepth]
maxMemo = [[-1, -1, -1] for n in range(N)]
for n in range(N-1):
    a, b = [int(l)-1 for l in input().split()]
    graph[a].append(b)
    graph[b].append(a)
startNode = None
for k in graph:
    if len(graph[k]) == 1:
        startNode = k
        break
makeData1(graph, set(), startNode, startNode, 0, maxMemo)
print(maxMemo)
