from collections import defaultdict
from typing import Tuple

# aのみが何通りありbのみが何通りありaとbを含むのが何通りあるか
def treeDP(graph: defaultdict[list], C: list[str], node: int, memo: list[bool])-> Tuple[int, int, int]:
    pass

N = int(input())
C = input().split()
graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
