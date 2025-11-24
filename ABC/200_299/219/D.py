def calc(X: int, Y: int, AB: list[list[int]])-> int:
    # data[(たこ焼き, たいやき)] = 弁当の個数の最小値
    base = 100000
    data = dict()
    data[0] = 0
    INF = len(AB) + 5
    result = INF
    for a, b in AB:
        newData = data.copy()
        for key in data:
            a2, b2 = key//base, key % base
            nxtA = min(a + a2, X + 1)
            nxtB = min(b + b2, Y + 1)
            nextKey = nxtA * base + nxtB
            newData[nextKey] = min(data[key] + 1, newData.get(nextKey, INF))
            if nxtA >= X and nxtB >= Y:
                result = min(newData[nextKey], result)
        data = newData
    return result if result != INF else -1


N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
print(calc(X, Y, AB))
