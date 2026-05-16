N, L, K, Y = map(int, input().split())
A = list(map(int, input().split()))
notOk = 0
count = 0
for a in A:
    if a <= L:
        notOk += 1
        continue
    if a - Y <= L:
        if count >= K:
                notOk += 1
                continue
        count += 1
print(N - notOk)
