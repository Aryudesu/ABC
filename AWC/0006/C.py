N, M, D = map(int, input().split())
T = list(map(int, input().split()))
res = 0
for t in T:
    if t <= M:
        continue
    k = (t - M) // D
    if (t - M) % D:
        k += 1
    res += k
print(res)
