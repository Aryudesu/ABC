N, M = map(int, input().split())
RData = [set() for _ in range(N)]
CData = [set() for _ in range(N)]
for _ in range(M):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    for p in RData[r]:
        CData[p].discard(r)
    for p in CData[c]:
        RData[p].discard(c)
    RData[r] = set()
    CData[c] = set()
    # print(RData, CData)
    RData[r].add(c)
    CData[c].add(r)
result = 0
for n in range(N):
    result += len(RData[n])
print(result)
