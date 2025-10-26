INF = 10**10
N, W = map(int, input().split())
ans = 0
# [価値] = 最小重さ
data = {0: 0}
for n in range(N):
    newData = data.copy()
    w, v = map(int, input().split())
    for nV in data:
        nW = data[nV]
        if nW + w > W:
            continue
        newData[nV + v] = min(nW + w, data.get(nV + v, INF))
        ans = max(ans, nV + v)
    data = newData
print(ans)
