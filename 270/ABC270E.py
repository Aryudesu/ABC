N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = []
c = 0
B = [a for a in A]
B.sort()
TN = N
TC = 0
MN = 0
Memo = 0
for n in range(N):
    # この一周で減らせる個数
    TmpB = B[n][0]
    if TmpB:
        TC += (N - n) * (TmpB - MN)
        MN = TmpB
    # 過剰になれば
    if TC > K:
        # 過剰分保存
        Memo = (TC - K)
        break
result = []
for a in A:
    # 引いた分
    tmp = a - MN
    if tmp > a:
        if Memo > 0:
            tmp += 1
            Memo -= 1
        result.append(str(tmp))
    else:
        result.append(str(0))
print(result)
