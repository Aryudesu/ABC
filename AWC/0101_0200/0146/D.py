def calcDiffList(M: int, S: list[str], C: list[str], T: list[str])->list[int]:
    result = []
    for base in range(M):
        co = 0
        for p in range(M):
            idx = (base + p) % M
            if C[p] == "1":
                continue
            if S[p] != T[idx]:
                co += 1
        result.append(co)
    return result

def calcBest(N: int, M: int, diffData: list[list[int]])->int:
    result = 10 ** 18
    for m in range(M):
        res = 0
        for n in range(N):
            res += diffData[n][m]
        result = min(result, res)
    return result

N, M, Q = map(int, input().split())
S = []
C = []
for _ in range(N):
    S.append(list(input()))
    C.append(list(input()))

T = [list(input()) for _ in range(N)]
diffData = [calcDiffList(M, S[n], C[n], T[n]) for n in range(N)]
# print(diffData)

result = []
for _ in range(Q):
    n, a, b, c = input().split()
    n, a, b = int(n), int(a), int(b)
    match n:
        case 1:
            S[a-1][b-1] = c
        case 2:
            C[a-1][b-1] = c
        case 3:
            T[a-1][b-1] = c
        case _:
            raise ValueError()
    diffData[a-1] = calcDiffList(M, S[a-1], C[a-1], T[a-1])
    result.append(calcBest(N, M, diffData))
print(*result, sep="\n")
