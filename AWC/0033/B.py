N, K, L, R = map(int, input().split())
T = list(map(int, input().split()))
result = 0
data = []
for t in T:
    if L <= t <= R:
        data.append(0)
    elif t < L:
        data.append(L - t)
    elif R < t:
        data.append(t - R)
data.sort()
# print(data)
print(sum(data[:K]))
