N, K = map(int, input().split())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

result = 0
l = 0
s1 = 0
s2 = 0
for r in range(N):
    s1 += B[r]
    s2 += A[r]
    while s1 > K and r >= l:
        s1 -= B[l]
        s2 -= A[l]
        l += 1
    result = max(result, s2)
print(result)
