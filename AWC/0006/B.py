N, K, T = map(int, input().split())
DR = []
for n in range(N):
    d, r = map(int, input().split())
    DR.append((d, r))
res = 0
for d, r in DR:
    if r >= K * d:
        res += r
print("Yes" if res >= T else "No")
# テストケース全部Noやんけ
