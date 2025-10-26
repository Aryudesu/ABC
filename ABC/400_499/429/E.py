from collections import defaultdict
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
def makeData(graph: dict[int, list[int]], data: dict[int, list[int]], node: int, memo: set[int], DS: str, s1: int, s2: int=10**10) -> list[int]:
    """
    TODO
    graphが渡される
    Sのときs1 = 0, s2 = s1 + 1で次のノードに渡す
    DFS起点はs2 = INF
    戻り値は最寄りのSのノードの距離2つ（昇順）
    """
    nextS1 = s1
    nextS2 = s2
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        if DS[nextNode] == "S":
            res1, res2 = makeData(graph, data, nextNode, memo, DS, 0, nextS1 + 1)
        else:
            res1, res2 = makeData(graph, data, nextNode, memo, DS, nextS1 + 1, nextS2 + 1)
        memo.discard(nextNode)
        if nextS1 > res2:
            nextS1 = res1
            nextS2 = res2
        elif nextS1 > res1:
            nextS2 = min(nextS1, res2)
            nextS1 = res1
        elif nextS2 > res1:
            nextS2 = res1
    data[node] = [nextS1, nextS2]
    return [nextS1 + 1, nextS2 + 1]

def updateData(graph: dict[int, list[int]], data: dict[int, list[int]], node: int, memo: set[int], DS: str, s1: int, s2: int=10**10) -> None:
    """開拓後に元ノードのデータ更新された場合を考慮する（根本の方が更新されてそうなので大丈夫？）"""
    nextS1 = s1
    nextS2 = s2
    res1, res2 = data[node]
    if nextS1 > res2:
        nextS1 = res1
        nextS2 = res2
    elif nextS1 > res1:
        nextS2 = min(nextS1, res2)
        nextS1 = res1
    elif nextS2 > res1:
        nextS2 = res1
    nextNodes = graph[node]
    for nextNode in nextNodes:
        if nextNode in memo:
            continue
        memo.add(nextNode)
        res1, res2 = updateData(graph, data, nextNode, DS, nextS1 + 1, nextS2 + 1)
        memo.discard(nextNode)
        if nextS1 > res2:
            nextS1 = res1
            nextS2 = res2
        elif nextS1 > res1:
            nextS2 = min(nextS1, res2)
            nextS1 = res1
        elif nextS2 > res1:
            nextS2 = res1
    data[node] = [nextS1, nextS2]
    return [nextS1 + 1, nextS2 + 1]

N, M = [int(l) for l in input().split()]
graph = defaultdict(list)
for m in range(M):
    u, v = [int(l) - 1 for l in input().split()] 
    graph[u].append(v)
    graph[v].append(u)
DS = input()
firstNode = None
for i in range(N):
    if DS[i] == "S":
        firstNode = i
        break
data = [[10**10, 10**10] for _ in range(N)]
makeData(graph, data, firstNode, {firstNode}, DS, 0)
for i in range(N):
    if DS[i] == "S":
        continue
    res1, res2 = data[i]
    print(res1 + res2)
