import bisect

N = int(input())
A = list({int(l) for l in input().split()})
N = len(A)
A.sort()
Q = int(input())
result = []
for _ in range(Q):
    b = int(input())
    idx = bisect.bisect_left(A, b)
    if idx >= 0 and idx < N:
        r = abs(b - A[idx])
    elif idx == N:
        idx = N - 1
        r = abs(b - A[idx])
    else:
        r = A[-1]
    if idx > 0:
        d2 = abs(b - A[idx - 1])
        r = min(r, d2)
    if idx + 1 < N:
        d2 = abs(b - A[idx + 1])
        r = min(r, d2)
    result.append(r)

for r in result:
    print(r)
