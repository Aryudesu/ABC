import sys

sys.setrecursionlimit(10**8)

N = int(input())
A = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
graph = dict()
data = []
n = 2
for p in P:
    tmp = graph.get(P[n-2], [])
    tmp.append(n)
    graph[P[n-2]] = tmp
    n += 1

def calc(node, depth):
    if len(data) <= depth:
        data.append(0)
    data[depth - 1] += A[node - 1]
    nodes = graph.get(node, [])
    for n in nodes:
        calc(n, depth + 1)

calc(1, 1)
s = 0
for d in range(len(data)):
    if data[- d - 1] != 0:
        s = data[-d - 1]
        break

if s > 0:
    print("+")
elif s < 0:
    print("-")
else:
    print("0")
