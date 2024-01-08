import sys

import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
graph = dict()
for n in range(N-1):
    a, b = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
result = set()
memo = [False for _ in range(N + 1)]

def calc(depth, n):
    if depth % 2:
        result.add(n)
    memo[n] = True
    nodes = graph.get(n, [])
    for node in nodes:
        if memo[node]:
            continue
        calc(depth + 1, node)
    memo[n] = False

memo[1] = True
calc(0, 1)
if len(result) < N//2:
    result_ = set()
    count = 0
    for i in range(1, N + 1):
        if not i in result:
            result_.add(i)
            count += 1
        if count >= N // 2:
            break
else:
    result_ = set()
    count = 0
    for i in range(1, N + 1):
        if i in result:
            result_.add(i)
            count += 1
        if count >= N // 2:
            break
print(*result_)
