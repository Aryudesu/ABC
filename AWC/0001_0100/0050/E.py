from atcoder.mincostflow import MCFGraph

N, M = map(int, input().split())
C = list(map(int, input().split()))
mcfg = MCFGraph(2 + N + M)
# 0 ~ N-1を警備会社，N～N+M-1を施設，N+Mをスタート，N+M+1をゴールとする
sNode = N + M
gNode = N + M + 1
shisetsuIdx = N
keibiIdx = 0
for n in range(N):
    E = list(map(int, input().split()))
    for m in range(M):
        if E[m] == 1:
            mcfg.add_edge(shisetsuIdx + m, keibiIdx + n, 1, C[n])

for m in range(M):
    mcfg.add_edge(sNode, shisetsuIdx + m, 1, 0)
for n in range(N):
    mcfg.add_edge(keibiIdx + n, gNode, 1, 0)
res = mcfg.flow(sNode, gNode)
if res[0] != M:
    print(-1)
else:
    print(res[1])
