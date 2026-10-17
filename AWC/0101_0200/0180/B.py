N, M = map(int, input().split())
S = input()
T = input()
result = 10 ** 18
for sIdx in range(N-M+1):
    res = 0
    for tIdx in range(M):
        res += S[sIdx + tIdx] != T[tIdx]
    result = min(res, result)
print(result)
