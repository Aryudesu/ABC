# 値, ビット列の長さ
data = [(0, 1), (1, 1)]
Q = int(input())
result = []
for q in range(Q):
    l, r, x = [int(l) for l in input().split()]
    i1, l1 = data[l]
    i2, l2 = data[r]
    tmp = (i1 << l2) | i2
    p = l1 + l2 - x
    result.append("1" if tmp & 1 << p else "0")
    data.append((tmp, l1 + l2))
for r in result:
    print(r)
