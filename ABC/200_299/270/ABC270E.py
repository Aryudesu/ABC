def is_ok(A, mid, K):
    count = 0
    for a in A:
        count += min([mid, a])
    return count <= K


N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
maxA = max(A)
l = -1
r = maxA + 1
while r - l > 1:
    mid = (l + r) // 2
    if is_ok(A, mid, K):
        l = mid
    else:
        r = mid
B = []
count = 0
for a in A:
    count += min([a, l])
    B.append(max([a - l, 0]))
amari = K - count
for idx in range(N):
    if amari:
        B[idx] -= 1
        amari -= 1
print(*B)
