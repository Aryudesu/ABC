from sortedcontainers import SortedSet

N, K = map(int, input().split())
R = []
D = []
data = SortedSet()
for idx in range(N):
    r, d = map(int, input().split())
    R.append(r)
    D.append(d)
    data.add((r, idx))
# print(R)
# print(D)
result = 0
for _ in range(K):
    r, idx = data.pop()
    result += r
    if idx - 1 >= 0:
        lKey = (R[idx-1], idx-1)
        if lKey in data:
            R[idx-1] -= D[idx]
            data.discard(lKey)
            data.add((R[idx-1], idx-1))
    if idx + 1 < N:
        rKey = (R[idx+1], idx+1)
        if rKey in data:
            R[idx+1] -= D[idx]
            data.discard(rKey)
            data.add((R[idx+1], idx+1))
print(result)
