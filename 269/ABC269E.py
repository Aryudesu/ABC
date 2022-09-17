N = int(input())
UN = 0
HN = N - 1
LN = 0
WN = N - 1
# 行の特定
for n in range(10):
    HHN = HN//2
    print(HHN)
    A, B, C, D = [1, N, UN, UN + HHN - 1]
    print('?', A, B, C + 1, D + 1)
    T = int(input())
    # 上半分が全て埋まってたら
    if HHN + 1 == T:
        UN = UN + HHN
    HN = HN - HHN
RYC = UN + 1
YHD = UN + 1
# 列の特定
for n in range(10):
    HWN = WN//2
    A, B, C, D = [LN, LN + HWN, 1, N]
    print('?', A + 1, B + 1, C, D)
    T = int(input())
    # 左半分が全て埋まってたら
    if HWN == T:
        LN = LN + HWN
    WN = WN - WN//2
RYA = LN + HWN
RYB = LN + HWN
print('!', RYC, RYA)
