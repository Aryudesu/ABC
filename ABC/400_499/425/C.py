N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = []
# 総和
s = 0
# 累積和
for a in A:
    s += a
    data.append(s)
# print(data)

result = []
# 先頭インデックス
idx = 0
for q in range(Q):
    n, *q = [int(l) for l in input().split()]
    if n == 1:
        c = q[0]
        idx = (idx + c) % N
    else:
        l, r = q
        l = (l + idx - 1) % N
        r = (r + idx - 1) % N
        if l <= r:
            tmp = data[r]
            if l > 0:
                tmp -= data[l - 1]
            result.append(tmp)
        else:
            tmp = data[l-1] - data[r]
            result.append(s - tmp)
        #     print("b")
        # print("debug", idx, l, r)
for r in result:
    print(r)
