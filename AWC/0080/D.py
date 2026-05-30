from atcoder.dsu import DSU
from typing import Tuple

def calc(N: int, WUVM: list[Tuple[int, int, int]], E: set[int])->bool:
    dsu = DSU(N)
    WUVM.sort()

    result = 0
    for w, u, v, m in WUVM:
        if m not in E:
            continue
        if dsu.same(u, v):
            return -1
        dsu.merge(u, v)
        result += w
    
    for w, u, v, m in WUVM:
        if m in E:
            continue
        if dsu.same(u, v):
            continue
        dsu.merge(u, v)
        result += w
    g = dsu.groups()
    if len(g) == 1:
        return result
    else:
        return -1

N, M, K = map(int, input().split())
WUVM = []
for m in range(M):
    u, v, w = map(int, input().split())
    WUVM.append((w, u - 1, v - 1, m))
E = set()
if K > 0:
    E = {int(l) - 1 for l in input().split()}
result = calc(N, WUVM, E)
print(result)
