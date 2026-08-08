from typing import Tuple

def calcData(mask: Tuple[int], graph: list[list[int]], PC: list[Tuple[int, int]]):
    result = 0
    b: int = mask
    while b:
        p = b.bit_length() - 1
        for q in graph[p]:
            if (1 << q) & mask == 0:
                return 0
        result += PC[p][0] - PC[p][1]
        b ^= (1 << p)
    return result

N, M = map(int, input().split())
PC = []
for n in range(N):
    p, c = map(int, input().split())
    PC.append((p, c))
graph = [[] for _ in range(N)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
result = 0
for mask in range(1 << N):
    result = max(result, calcData(mask, graph, PC))
print(result)
