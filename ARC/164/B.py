import sys

sys.setrecursionlimit(2 * 10**5)

N, M = [int(l) for l in input().split()]
graph = dict()
for m in range(M):
    a, b = [int(l) for l in input().split()]
    tmp = graph.get(a, [])
    tmp.append(b)
    graph[a] = tmp
    tmp = graph.get(b, [])
    tmp.append(a)
    graph[b] = tmp
C = [int(l) == 0 for l in ("1 " + input()).split()]
data = [False] * (N + 1)
mem = [False] * (N + 1)


def calc(node):
    mem[node] = True
    # 既に来たことあるノードに到着すると来た順に戻って1に到着すれば良い
    if data[node]:
        return True
    # 探索
    tmp = graph.get(node, [])
    for n in tmp:
        if C[node] != C[n]:
            C[node] = not C[node]
            data[node] = True
            if calc(n):
                return True
            C[node] = not C[node]
            data[node] = False
    return False


def search():
    for n in range(1, N + 1):
        if not mem[n]:
            if calc(n):
                return True
    return False


print("Yes" if search() else "No")
