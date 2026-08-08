N, M = map(int, input().split())
S = list(map(int, input().split()))
for m in range(M):
    t, v = map(int, input().split())
    S[t-1] = max(S[t-1] + v, 0)
print(*S)
