N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
c = min(C)
l = 0
s = 0
result = 0
for r in range(N):
    s += W[r]
    while s > c and r - l > 0:
        s -= W[l]
        l += 1
    if s <= c:
        result += r - l + 1
print(result)
