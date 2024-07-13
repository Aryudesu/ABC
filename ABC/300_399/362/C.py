def calc(N, LR):
    s = 0
    for l, r in LR:
        s += l
    if s > 0:
        print("No")
        return
    result = []
    s *= -1
    for l, r in LR:
        tmp = l
        if s > 0:
            if s + l > r:
                tmp = r
                s -= r - l
            else:
                tmp = s + l
                s = 0
        result.append(tmp)
    if s == 0:
        print("Yes")
        print(*result)
    else:
        print("No")



N = int(input())
LR = []
for n in range(N):
    L, R = [int(l) for l in input().split()]
    LR.append([L, R])
calc(N, LR)
