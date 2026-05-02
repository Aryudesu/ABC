from atcoder.dsu import DSU

N, Q = map(int, input().split())
card = [-1] * N
for _ in range(Q):
    c, p = map(int, input().split())
    c, p = c - 1, p - 1
    card[c] = p
dsu = DSU(N)
for i in range(N):
    if card[i] >= 0:
        dsu.merge(card[i], i)
result = []
for i in range(N):
    if card[i] != -1:
        result.append(0)
    else:
        result.append(dsu.size(i))
print(*result)
