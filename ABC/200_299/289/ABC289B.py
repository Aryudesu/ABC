N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
num = [[None, n+1, None]for n in range(N)]
for a in A:
    tmp = num[a]
    tmp[0] = a-1
    num[a] = tmp
    tmp = num[a-1]
    tmp[2] = a
    num[a-1] = tmp
result = []
for n in num:
    if n[2] is None:
        tmp = n[0]
        result.append(n[1])
        while not tmp is None:
            t_ = num[tmp]
            result.append(t_[1])
            tmp = t_[0]
print(*result)
