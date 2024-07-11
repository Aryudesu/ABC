from atcoder.segtree import SegTree

N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
Data = [(0, 0, a, 1) for a in A]

# 最大値計算用
MX1 = 10 ** 10
def op1(a, b):
    a1, a1c, a2, a2c = a
    b1, b1c, b2, b2c = b
    m1, m1c, m2, m2c = a1, a1c, a2, a2c
    if b1 > m2:
        m1 = m2
        m1c = m2c
        m2 = b1
        m2c = b1c
    elif b1 == m2:
        m2c += b1c
    elif b1 > m1:
        m1 = b1
        m1c = b1c
    elif b1 == m1:
        m1c += b1c
    if b2 > m2:
        m1 = m2
        m1c = m2c
        m2 = b2
        m2c = b2c
    elif b2 == m2:
        m2c += b2c
    elif b2 > m1:
        m1 = b2
        m1c = b2c
    elif b2 == m1:
        m1c += b2c
    return (m1, m1c, m2, m2c)
e1 = (0, 0, 0, 0)
ST1 = SegTree(op1, e1, Data)

result = []
for _ in range(Q):
    x, y, z = [int(l) for l in input().split()]
    if x == 1:
        p, x = y - 1, z
        ST1.set(p, (0, 0, x, 1))
    else:
        l, r = y, z
        tmp = ST1.prod(l-1, r)
        result.append(tmp[1])
for r in result:
    print(r)
