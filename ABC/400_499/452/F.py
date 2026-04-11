from sortedcontainers import SortedSet

N, K = map(int, input().split())
P = list(map(int, input().split()))
data = SortedSet()
l = 0
s = 0
result = 0
for r in range(N):
    p = P[r]
    tmp = data.bisect_left(-p)
    s += tmp
    data.add(-p)
    while s > K and r > l:
        pl = P[l]
        tmp2 = data.bisect_left(-pl)
        data.discard(-pl)
        s -= len(data) - tmp2
        l+=1
    if s == K:
        # print("debug", f"({l+1}, {r+1})")
        result += 1
while s == K and l < N:
    pl = P[l]
    tmp2 = data.bisect_left(-pl)
    data.discard(-pl)
    s -= len(data) - tmp2
    l+=1
    if s == K:
        # print("debug", f"({l+1}, {r+1})")
        result += 1
    else:
        break
print(result)
