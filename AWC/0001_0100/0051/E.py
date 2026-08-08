from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
ft = FenwickTree(N + 1)
G = []
for m in range(M):
    g = int(input())
    ft.add(g, 1)
    G.append(g)
result = 0
for g in G:
    ft.add(g, -1)
    result += ft.sum(0, g)
print(result)