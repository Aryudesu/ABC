N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = dict()
for idx in range(N):
    a = A[idx]
    tmp = data.get(a, [])
    tmp.append(idx + 1)
    data[a] = tmp
print(data)
result = []
for _ in range(Q):
    x, k = [int(l) for l in input().split()]
    tmp = data.get(x, [])
    if k - 1 < len(tmp):
        result.append(tmp[k-1])
    else:
        result.append(-1)

for r in result:
    print(r)
