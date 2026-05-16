from typing import Tuple
def calc(N: int, K: int, D: int, XP: list[Tuple[int, int]])->int:
    # X座標昇順
    XP.sort()
    result = 0

    # 電波塔の候補
    denpaKouho = []
    if XP[0][1] >= K:
        denpaKouho.append(XP[0][0])

    prev = None
    # 電波が届かなくなった最小値
    minX = XP[0][0]

    for idx in range(1, N):
        x, p = XP[idx]
        if prev is not None:
            if abs(prev - x) <= D:
                if p >= K:
                    denpaKouho.append(x)
            else:
                minX = x
        # print(idx, x, minX)
        if x - minX <= D:
            if p >= K:
                denpaKouho.append(x)
        else:
            if len(denpaKouho) == 0:
                return -1
            prev = denpaKouho[-1]
            result += 1
            minX = prev
            denpaKouho = []
            if p >= K:
                denpaKouho.append(x)
    if XP[-1][0] - prev > D:
        if len(denpaKouho) == 0:
            return -1
        else:
            result += 1
    return result


N, K, D = map(int, input().split())
XP = []
for n in range(N):
    x, p = map(int, input().split())
    XP.append((x, p))
print(calc(N, K, D, XP))
