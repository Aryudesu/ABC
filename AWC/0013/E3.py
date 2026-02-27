from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
mf = MFGraph(N + M + 2)
s = N + M
t = N + M + 1
for n in range(N):
    mf.add_edge(s, n, 1)
for m in range(M):
    mf.add_edge(N + m, t, 1)

for n in range(N):
    K, *C = list(map(int, input().split()))
    for c in C:
        mf.add_edge(n, N + c-1, 1)

print(mf.flow(s, t))
