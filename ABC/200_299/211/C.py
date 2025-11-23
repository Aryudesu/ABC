from collections import defaultdict

# 下準備
sToNum = defaultdict(int)
S = "chokudai"
for idx in range(len(S)):
    sToNum[S[idx]] = idx
MOD = 10**9 + 7
check = set(list(S))

# メイン部分
S = input()
count = [0] * 8
result = 0
for s in S:
    if not s in check:
        continue
    num = sToNum[s]
    if num > 0:
        count[num] = (count[num] + count[num - 1]) % MOD
    else:
        count[num] = (count[num] + 1) % MOD
print(count[-1])
