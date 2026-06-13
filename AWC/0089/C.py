N, B = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
l = 0
c = 0
p = P[0]
result = 0
for r in range(N-1):
    p += P[r + 1]
    c += C[r]
    while c > B:
        p -= P[l]
        c -= C[l]
        l += 1
    result = max(result, p)
print(result)
