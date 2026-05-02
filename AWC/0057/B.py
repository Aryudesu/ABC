def is_subsequence(S: str, T: str)->bool:
    """TがSの部分列か"""
    if len(T) == 0:
        return True
    if len(T) > len(S):
        return False
    tIdx = 0
    for s in S:
        if s == T[tIdx]:
            tIdx += 1
            if tIdx == len(T):
                return True
    return len(T) == 0

N = int(input())
idxData = []
SDatas = []
for n in range(N):
    k, *S = input().split()
    SDatas.append(S)
Q = int(input())
result = []
for _ in range(Q):
    T = input()
    res = 0
    for SData in SDatas:
        for S in SData:
            if is_subsequence(S, T):
                res += 1
                break
    result.append(res)
for r in result:
    print(r)
