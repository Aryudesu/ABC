def calc(N: int, M: int, LR: list[int])->int:
    data = []
    prevL, prevR = 0, 0
    kouhoL, kouhoR = 0, 0
    for m in range(M):
        l, r = LR.pop()
        if prevR + 1 < l:
            if prevR + 1 < kouhoL:
                return -1
            data.append((kouhoL, kouhoR))
            if kouhoR == N:
                # print(data)
                return len(data)
            prevL, prevR = kouhoL, kouhoR
            kouhoL, kouhoR = l, r
        else:
            # print(l, r, prevL, prevR, kouhoL, kouhoR)
            if kouhoR < r:
                kouhoL, kouhoR = l, r
    if prevR + 1 < kouhoL:
        return -1
    if kouhoR != N:
        return -1
    data.append((kouhoL, kouhoR))
    # print(data)
    return len(data)


N, M = map(int, input().split())
LR = []
for m in range(M):
    l, r = map(int, input().split())
    LR.append((l, r))
LR.sort(reverse=True)
print(calc(N, M, LR))
