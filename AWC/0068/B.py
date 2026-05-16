N, M = map(int, input().split())
A = list(map(int, input().split()))
data = []
for m in range(M):
    l, r = map(int, input().split())
    s = 0
    for idx in range(l-1, r):
        s += A[idx]
    data.append((l, s))
data.sort()
print(max(s for l, s in data) - min(s for l, s in data))
