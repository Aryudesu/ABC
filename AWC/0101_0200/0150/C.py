N, M = map(int, input().split())
P = list(map(int, input().split()))
data = [False] * M
for p in P:
    q = p - 1
    if data[q]:
        for n in range(q + 1, M):
            if not data[n]:
                data[n] = True
                break
    else:
        data[q] = True
print(sum(data))
