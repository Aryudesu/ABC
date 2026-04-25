def isOk(infect: list[int], notInfect: list[int], data: int)->bool:
    # 感染
    for ift in infect:
        if data & ift == 0:
            return False
    # 感染していない    
    for nift in notInfect:
        if data & nift != 0:
            return False
    return True
    

N, M = map(int, input().split())
infect = []
notInfect = []
for m in range(M):
    k, *S, r = list(map(int, input().split()))
    b = 0
    for s in S:
        b |= (1 << (s-1))
    if r == 1:
        infect.append(b)
    else:
        notInfect.append(b)


# 感染 = 1, not感染 = 0
result = N
for mask in range(1 << N):
    if isOk(infect, notInfect, mask):
        result = min(result, mask.bit_count())
print(result)
