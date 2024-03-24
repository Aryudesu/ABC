import math

N, a, b, c = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
M = a * b * c
Data = []
for n in range(N):
    Data.append([0, 0, 0, 0, 0, 0, 0])
for n in range(N):
    Data[n][0] = a - (A[n] % a) if A[n] % a else 0
    Data[n][1] = b - (A[n] % b) if A[n] % b else 0
    Data[n][2] = c - (A[n] % c) if A[n] % c else 0
    abgcd = math.gcd(a, b)
    ab = (a * b) // abgcd
    Data[n][3] = ab - (A[n] % ab) if A[n] % ab else 0
    acgcd = math.gcd(a, c)
    ac = (a * c) // acgcd
    Data[n][4] = ac - (A[n] % ac) if A[n] % ac else 0
    bcgcd = math.gcd(b, c)
    bc = (b * c) // bcgcd
    Data[n][5] = bc - (A[n] % bc) if A[n] % bc else 0
    abc = (a * b) // abgcd
    abcgcd = math.gcd(abc, c)
    abc = (abc * c) // abcgcd
    Data[n][6] = abc - (A[n] % abc) if A[n] % abc else 0
# 最小Topいくつを拾ってくるか
K = min(3, N)
Top = []
for i in range(K):
    tmp = []
    for j in range(7):
        tmp.append([M, None])
    Top.append(tmp)
for n in range(N):
    for i in range(7):
        d = Data[n][i]
        for k in range(K):
            if Top[k][i][0] > d:
                for l in range(K - 1 - k):
                    Top[K - l - 1][i] = Top[K - l - 2][i]
                Top[k][i] = [d, n]
                break
# for t in Top:
#     print(t)
I = [1, 2, 4, 3, 5, 6, 7]
result = M
if N >= 3:
    for i in range(7 * K):
        iIdx = Top[i // 7][i % 7][1]
        for j in range(7 * K):
            jIdx = Top[j // 7][j % 7][1]
            for k in range(7 * K):
                kIdx = Top[k // 7][k % 7][1]
                if iIdx != jIdx and jIdx != kIdx and iIdx != kIdx:
                    if (I[i % 7] | I[j % 7] | I[k % 7]) == 7:
                        tmp = (
                            Top[i // 7][i % 7][0]
                            + Top[j // 7][j % 7][0]
                            + Top[k // 7][k % 7][0]
                        )
                        if result > tmp:
                            # print(i, j, k, tmp)
                            result = tmp
if N >= 2:
    for i in range(7 * K):
        iIdx = Top[i // 7][i % 7][1]
        for j in range(7 * K):
            jIdx = Top[j // 7][j % 7][1]
            if iIdx != jIdx:
                if (I[i % 7] | I[j % 7]) == 7:
                    tmp = Top[i // 7][i % 7][0] + Top[j // 7][j % 7][0]
                    if result > tmp:
                        # print(i, j, tmp)
                        result = tmp
if N >= 1:
    for i in range(7 * K):
        if I[i % 7] == 7:
            if result > Top[i // 7][i % 7][0]:
                # print(i, tmp)
                result = Top[i // 7][i % 7][0]
print(result)
