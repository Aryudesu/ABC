N = int(input())
for n in range(N):
    res = []
    tmp = [int(l) for l in input().split()]
    for n in range(N):
        if tmp[n] == 1:
            res.append(n + 1)
    print(*res)
