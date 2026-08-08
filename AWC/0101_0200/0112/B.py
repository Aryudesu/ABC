INF = 10**16
N, M, K = map(int, input().split())
D = list(map(int, input().split()))
S = [-INF] * N
for m in range(M):
    p, s = map(int, input().split())
    S[p-1] = s
E = K
isOk = True
for n in range(N):
    if E <= 0:
        isOk = False
        break
    E -= D[n]
    if S[n] > E:
        E = S[n]
print("Yes" if isOk else "No")
