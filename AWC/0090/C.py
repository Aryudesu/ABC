from collections import defaultdict
from typing import Tuple
import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


N, M = map(int, input().split())
LRDATA = []
PQDATA = []
ISOK = [True] * N
NODECHECK = [False] * N
for n in range(N):
    l, r, p, q = map(int, input().split())
    LRDATA.append((l-1, r-1))
    PQDATA.append((p, q))

graphCheck = True
inCount = defaultdict(int)
graph = defaultdict(list)
for m in range(M):
    u, v, b = map(int, input().split())
    graph[u-1].append((b, v - 1))
    inCount[v-1] += 1
    if inCount[v-1] > 1:
        graphCheck = False
if inCount[0] > 0:
    graphCheck = False

if not graphCheck:
    print("NO")
    exit(0)

def calc(N: int, M: int, node: int, graph: dict[int, list[Tuple[int, int]]]):
    NODECHECK[node] = True
    nextNodes = graph[node]
    if len(nextNodes) > 2:
        ISOK[node] = False
        return
    if len(nextNodes) == 2:
        a, b = nextNodes[0][0], nextNodes[1][0]
        if a + b != 1:
            ISOK[node] = False
            return
    # 終点の場合は終点のノードを返却する
    if len(nextNodes) == 0:
        return

    nowL, nowR = LRDATA[node]
    memo = [None, None]
    for b, nextNode in nextNodes:
        l, r = LRDATA[nextNode]
        if not (nowL < l and r < nowR):
            ISOK[node] = False
            return
        if not (PQDATA[nextNode][0] == PQDATA[node][1]):
            ISOK[node] = False
            return
        calc(N, M, nextNode, graph)
        memo[b] = nextNode
    if len(nextNodes) == 2 and not (LRDATA[memo[0]][1] < LRDATA[memo[1]][0]):
            ISOK[node] = False
            return

calc(N, M, 0, graph)
nodeCheck = False not in NODECHECK
getCheck = False not in ISOK
print("YES" if nodeCheck and getCheck else "NO")
