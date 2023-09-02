def calc(data, check, k):
    # 全て通過済か
    tmp = True
    for c in check:
        if not check.get(c, False):
            tmp = False
    # 全て通過した場合はTrueを返す
    if tmp:
        return True
    # 抜けがある場合，そこから繋げられるもの全走査
    keys = data.get(k, [])
    for key in keys:
        # 通過済は無視
        if check.get(key):
            continue
        # 通過していない場合
        check[key] = True
        if calc(data, check, key):
            return True
        check[key] = False
    return False


N, M = [int(l) for l in input().split()]
S = [input() for _ in range(N)]
data = dict()
for i in range(N - 1):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(M):
            if S[i][k] != S[j][k]:
                tmp += 1
                if tmp > 1:
                    break
        if tmp == 1:
            t = data.get(S[i], [])
            t.append(S[j])
            data[S[i]] = t
            t = data.get(S[j], [])
            t.append(S[i])
            data[S[j]] = t
check = {s: False for s in S}
result = False
for s in S:
    r = calc(data, check, s)
    if r:
        result = True
        break
print("Yes" if result else "No")
