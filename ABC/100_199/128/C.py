def isOk(num: int, switchData: list[int], P: list[int])->bool:
    # 各電球に対して
    for p, s in zip(P, switchData):
        if ((num & s).bit_count()) % 2 != p:
            return False
    return True

N, M = map(int, input().split())
S = []
for m in range(M):
    k, *SW = list(map(int, input().split()))
    tmp = 0
    for sw in SW:
        tmp |= (1 << (sw-1))
    S.append(tmp)
P = list(map(int, input().split()))
result = 0
for num in range(1 << N):
    if isOk(num, S, P):
        result += 1
print(result)
