def calc(N):
    res = []
    for n in range(N+1):
        tmp = 1
        for k in range(n):
            tmp *= N-k
        for k in range(n + 1):
            if k != 0:
                tmp = tmp // k
        res.append(str(tmp))
    print(*res)


N = int(input())
for n in range(N):
    calc(n)
