N = int(input())
D = [int(l) for l in input().split()]

for i in range(N-1):
    tmp = 0
    res = []
    for j in range(i, N-1):
        tmp += D[j]
        res.append(tmp)
    print(*res)
