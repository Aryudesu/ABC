N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = 0
w = 0
h = 0
result = 0
for r in range(N):
    w += B[r]
    h += A[r]
    while w > K:
        w -= B[l]
        h -= A[l]
        l += 1
    # print(l, r)
    result = max(result, h)
print(result)
