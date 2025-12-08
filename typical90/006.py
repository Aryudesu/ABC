# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N
def calc_nex(S):
    N = len(S)
    res = [[N] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(S[i]) - ord('a')] = i
    return res

N, K = [int(l) for l in input().split()]
S = input()
nex = calc_nex(S)
# 貪欲法
res = ""
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]

        # ちゃんと K 文字が作れれば OK
        if N - k >= K - i:
            res += chr(ord('a') + ordc)
            j = k
            break
print(res)
