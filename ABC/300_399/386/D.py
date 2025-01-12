def calc(N, data, Y):
    # とっていないといけないBの最大値
    bMax = 0
    # 右から見ていく
    for y in Y:
        yData = data.get(y, dict())
        # 次にとらないといけないBとWの最大値
        bTmp = yData.get("B")
        wTmp = yData.get("W")
        if not wTmp is None:
            if wTmp <= bMax:
                return False
        if not bTmp is None and not wTmp is None:
            if bTmp > wTmp:
                return False
        if not bTmp is None:
            bMax = max([bMax, bTmp])
    return True

N, M = [int(l) for l in input().split()]
data = dict()
Y = []
memo = set()
for m in range(M):
    x, y, c = input().split()
    x, y = int(x), int(y)
    tmp = data.get(y, dict())
    if c == "B":
        bmax = tmp.get("B", -1)
        tmp["B"] = max([bmax, x])
    else:
        bmax = tmp.get("W", N + 1)
        tmp["W"] = min([bmax, x])
    data[y] = tmp
    if not y in memo:
        Y.append(y)
        memo.add(y)
Y.sort(reverse=True)
print("Yes" if calc(N, data, Y) else "No")
