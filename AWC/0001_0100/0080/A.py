N, M = map(int, input().split())
H = list(map(int, input().split()))
for m in range(M):
    t, d = map(int, input().split())
    t -= 1
    if t-1 >= 0:
        H[t-1] -= d//2
    if t+1 < N:
        H[t+1] -= d//2
    H[t] -= d
print(sum(h>=1 for h in H))
