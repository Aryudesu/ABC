def is_same_sgn(a, b):
    return a * b >= 0

N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = []
# 各idx = 0 ~ N-1 の [idx + 1] - [idx]
for idx in range(N - 1):
    data.append(A[idx + 1] - A[idx])
res = 0
for d in data:
    res += abs(d)
result = []
for _ in range(Q):
    L, R, V = [int(l) for l in input().split()]
    L -= 1
    R -= 1
    if L > 0:
        res -= abs(data[L-1])
        data[L - 1] += V
        res += abs(data[L-1])
    if R < N-1:
        res -= abs(data[R])
        data[R] -= V
        res += abs(data[R])
    result.append(res)

for r in result:
    print(r)
