N = int(input())

UN = 0
HN = N
# 行の特定
for n in range(10):
    HHN = HN//2
    if HHN == 0:
        break
    A, B, C, D = [1, N, UN, UN + HHN - 1]
    print('?', A, B, C + 1, D + 1)
    T = int(input())
    # 上半分が全て埋まってたら
    if HHN == T:
        UN = UN + HHN
    HN = HN - HHN
RYC = UN + 1
YHD = UN + 1

LN = 0
WN = N
# 列の特定
for n in range(10):
    HWN = WN//2
    if HWN == 0:
        break
    A, B, C, D = [LN, LN + HWN - 1, 1, N]
    print('?', A + 1, B + 1, C, D)
    T = int(input())
    # 左半分が全て埋まってたら
    if HWN == T:
        LN = LN + HWN
    WN = WN - HWN
RYA = LN + 1
RYB = LN + 1

print('!', RYC, RYA)
