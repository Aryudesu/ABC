N = int(input())
# 持ってる本
A = {int(l) for l in input().split()}
LA = len(A)
AMAX = max(A)
DF = list(A)
DF.sort()
LDF = len(DF)
# 重複分
dup = N - LA
SOLD = dup % 2
# 重複分売れ残り
dup = dup - SOLD
R = 0
res = 0
while True:
    res += 1
    n = res
    # 該当の本を持っていない時
    if n not in A:
        # ダブった本を売る
        if dup >= 2:
            dup -= 2
        # ダブった本がなくなった場合
        else:
            if SOLD:
                if 1 + (2 * R) > LDF:
                    res -= 1
                    break
                if DF[-1 - (2 * R)] > n:
                    R += 1
                else:
                    res -= 1
                    break
            else:
                if 2 * (R + 1) > LDF:
                    res -= 1
                    break
                if DF[- (2 * (R + 1))] > n:
                    R += 1
                else:
                    res -= 1
                    break
            pass
print(res)
