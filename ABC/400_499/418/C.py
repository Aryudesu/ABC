import bisect

N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
data = []
s = 0
for a in A:
    s += a
    data.append(s)
# print(A)
# print(data)
result = []
for q in range(Q):
    B = int(input())
    if B > A[-1]:
        result.append(-1)
        continue
    idx = bisect.bisect_left(A, B)
    # print("idx", B, idx)
    if idx == 0:
        result.append((N-idx) * (B - 1) + 1)
    else:
        result.append(data[idx - 1] + (N-idx) * (B - 1) + 1)
for r in result:
    print(r)
