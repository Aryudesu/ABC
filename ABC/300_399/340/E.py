from atcoder.fenwicktree import FenwickTree

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
data = [a for a in A]
# 全体に行き渡るボールの量
allBalls = 0
# いもす法をフェニ木でやってみる？
ft = FenwickTree(N)
for m in range(M):
    # B[m]に入っているボールの個数
    bb = B[m]
    b = data[bb] + ft.sum(0, bb + 1) + allBalls
    # ボールすべて取り出す
    data[bb] -= b
    # 全体に回す個数
    allBalls += b // N
    if b % N != 0:
        l = (bb + 1) % N
        r = (bb + b) % N
        if l > r:
            ft.add(0, 1)
            if r + 1 < N:
                ft.add(r + 1, -1)
            ft.add(l, 1)
        else:
            ft.add(l, 1)
            if r + 1 < N:
                ft.add(r + 1, -1)
result = []
for n in range(N):
    s = ft.sum(0, n + 1)
    result.append(data[n] + s + allBalls)
print(*result)