import sys

sys.setrecursionlimit(10**6)

N = int(input())
A = [int(l) for l in input().split()]
graph = dict()
result = []
last = None
#graph[前の人] = 後ろの人
for i in range(len(A)):
    if A[i] == N - 1:
        last = i
    graph[A[i]] = i + 1

# print(graph)

def calc(n):
    node = graph.get(n)
    if node is None:
        return
    result.append(node)
    calc(node)

calc(-1)
print(*result)
