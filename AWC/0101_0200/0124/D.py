N, K = map(int, input().split())
W = []
S = []
for n in range(N):
    w, s = map(int, input().split())
    W.append(w)
    S.append(s)
if sum(W) >= K:
    print(sum(S))
else:
    print(-1)
