from math import isqrt

T = int(input())
result = []
for t in range(T):
    c, d = [int(l) for l in input().split()]
    c1 = str(c + 1)
    cd = str(c + d)
    if len(c1) != len(cd):
        # 繰り上げ時
        pass
    else:
        # 繰り上げしないとき
        pass
