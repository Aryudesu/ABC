N, K = [int(l) for l in input().split()]
count = 0
for n in range(1, N + 1):
    lp = min([N, K - n])
    for m in range(1, lp + 1):
        tmp = K - (n + m)
        if tmp <= N and tmp >= 1:
            count += 1
print(count)
