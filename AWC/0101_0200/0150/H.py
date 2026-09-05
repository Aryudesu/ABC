N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
lIdx = 0
rIdx = N-1
l = A[lIdx]
r = A[rIdx]
result = r - l
for _ in range(K-1):
    d1 = abs(A[lIdx + 1] - r)
    d2 = abs(A[lIdx + 1] - l)
    d3 = abs(A[rIdx - 1] - r)
    d4 = abs(A[rIdx - 1] - l)
    if max(d1, d2, d3) <= d4:
        result += d4
        l = A[rIdx - 1]
        rIdx -= 1
    elif max(d1, d2, d4) <= d3:
        result += d3
        r = A[rIdx - 1]
        rIdx -= 1
    elif max(d1, d3, d4) <= d2:
        result += d2
        l = A[lIdx + 1]
        lIdx += 1
    elif max(d2, d3, d4) <= d1:
        result += d1
        r = A[lIdx + 1]
        lIdx += 1
print(result)
