def isOk(N, TX):
    data = dict()
    for n in range(N):
        t, x = TX[n]
        if t == 1:
            data[x] = data.get(x, 0) + 1
        else:
            data[x] = data.get(x, 0) - 1
        if data[x] < 0:
            return False
    return True


def calcMin(N, TX):
    result = 0
    count = 0
    data = dict()
    koudou = []
    for n in range(N):
        t, x = TX[ -n - 1]
        # モンスターを倒すためのポーション
        if t == 2:
            data[x] = data.get(x, 0) + 1
            count += 1
        else:
            # モンスターを倒すためのポーションを拾う必要がある
            if data.get(x, 0) > 0:
                # 最大値更新
                if count > result:
                    result = count
                data[x] = data.get(x, 0) - 1
                count -= 1
                koudou.append(1)
            else:
                koudou.append(0)
    koudou = koudou[::-1]
    return result, koudou


def calc(N, TX):
    if not isOk(N, TX):
        return -1, []
    return calcMin(N, TX)



N = int(input())
TX = []
for n in range(N):
    t, x = [int(l) for l in input().split()]
    TX.append((t, x))
res, koudou = calc(N, TX)
if res < 0:
    print(res)
else:
    print(res)
    print(*koudou)
