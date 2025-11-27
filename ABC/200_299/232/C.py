from itertools import permutations
from collections import defaultdict

def calc(data: list[int], N: int, M: int, AB: dict[int, int], CD: dict[int, int])-> bool:
    for a in range(N):
        for b in AB[a]:
            c = data[a]
            d = data[b]
            if not d in CD[c]:
                return False
    return True


N, M = [int(l) for l in input().split()]
abGraph = defaultdict(set)
cdGraph = defaultdict(set)
for m in range(M):
    a, b = map(int, input().split())
    abGraph[a-1].add(b-1)
    abGraph[b-1].add(a-1)
for m in range(M):
    c, d = map(int, input().split())
    cdGraph[c-1].add(d-1)
    cdGraph[d-1].add(c-1)

result = False
for data in permutations(range(N)):
    if calc(data, N, M, abGraph, cdGraph):
        result = True
        break
print("Yes" if result else "No")
