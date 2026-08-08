N, M = map(int, input().split())
manzoku = [0] * (M + 1)
for n in range(N):
    t, p = map(int, input().split())
    for yen in range(M+1, -1, -1):
        if yen + t > M:
            continue
        manzoku[yen + t] = max(manzoku[yen] + p, manzoku[yen + t])
print(max(manzoku))
