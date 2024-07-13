import sys

sys.setrecursionlimit(10**6)

def calc(num: int, graph: list, memo: set, result: list):
    nodes = graph[num]
    memo.add(num)
    for node in nodes:
        if node in memo:
            continue
        calc(node, graph, memo, result)
    result.append(num+1)

N = int(input())
P = []
for n in range(N):
    c, *p = [int(l) - 1 for l in input().split()]
    P.append(p)
res = []
calc(0, P, set(), res)
result = [res[i] for i in range(len(res) - 1)]
print(*result)
