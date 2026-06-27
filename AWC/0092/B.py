def calc(x: int, v: int, L: int, T: int)->int:
    # 移動距離計算
    diff = (v * T) % (2 * L)
    if v < 0:
        diff = -(((-v) * T) % (2 * L))
    if v > 0:
        if x + diff > L:
            newDiff = x + diff - L
            if newDiff >= L:
                return newDiff - L
            else:
                return L - newDiff
        return x + diff
    elif v < 0:
        if x + diff < 0:
            newDiff = abs(x + diff)
            if newDiff >= L:
                return L - (newDiff - L)
            else:
                return newDiff
        return x + diff
    else:
        return x


N, L, T = map(int, input().split())
result = []
for n in range(N):
    x, v = map(int, input().split())
    result.append(calc(x, v, L, T))

for r in result:
    print(r)
