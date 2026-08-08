from typing import Tuple
import pypyjit
import sys
sys.setrecursionlimit(20**6)
pypyjit.set_param('max_unroll_recursion=-1')

def calc(memo: set[Tuple[int, int]], goal: int, node: int, graph: list[list[Tuple[int, int]]], key: set[int], PC: list[int])->bool:
    c = PC[node]
    if c != 0:
        key.add(c)
    isIn = c in key
    if node == goal:
        return True
    l = len(key)
    if (node, l) in memo:
        return False
    memo.add((node, l))
    for nextNode, k in graph[node]:
        if k not in key:
            continue
        res = calc(memo, goal, nextNode, graph, key, PC)
        if res:
            return True
    if not isIn:
        key.discard(c)
    return False

N, M = map(int, input().split())
PC = [0] * N
for n in range(N):
    p, c = map(int, input().split())
    PC[n] = c
K = [0] * N
graph = [[] for _ in range(N)]
for m in range(M):
    u, v, k = map(int, input().split())
    if u == v:
        continue
    graph[u-1].append((v-1, k))
memo = set()
key = set()
res = calc(memo, N-1, 0, graph, key, PC)
print("Yes" if res else "No")
