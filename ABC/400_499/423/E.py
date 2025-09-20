N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
s = 0
s2 = 0
data1 = []
data2 = []
for i in range(N):
    s += A[i] * (i + 1)
    s2 += A[i]
    data1.append(s)
    data2.append(s2)
result = []
for q in range(Q):
    l, r = [int(l) - 1 for l in input().split()]
    res = data1[r] - data1[max(l, 0)]
    res -= data2[l] * (r - l - 1)
    result.append(res)
# print(data1, data2)
for r in result:
    print(r)
