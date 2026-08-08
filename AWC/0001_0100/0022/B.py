N, M, T = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for a in A:
    if T - a > 0:
        res += T - a
print(-1 if res > M else res)
