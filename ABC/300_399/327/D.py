import sys

sys.setrecursionlimit(10**6)

N, M = [int(l) for l in input().split()]
A = [int(l)-1 for l in input().split()]
B = [int(l)-1 for l in input().split()]
graph = dict()
for m in range(M):
    a = A[m]
    b = B[m]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
data = [False] * N
result = [0] * N


def calc(node, color):
    data[node] = True
    result[node] = color
    gra = graph.get(node, [])
    for n in gra:
        if not data[n]:
            calc(n, -color)


def check():
    for m in range(M):
        gra = graph.get(m, [])
        for g in gra:
            if result[g] == result[m]:
                return False
    return True


for n in range(N):
    if not data[n]:
        calc(n, 1)
print("Yes" if check() else "No")
