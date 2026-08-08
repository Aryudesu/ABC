N, M = map(int, input().split())
W = []
L = []
for n in range(N):
    w, l = map(int, input().split())
    W.append(w)
    L.append(l)
for m in range(M):
    p, c = map(int, input().split())
    W[p-1] += c
print(sum(w > l for w, l in zip(W, L)))

