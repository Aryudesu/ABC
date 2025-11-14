from sortedcontainers import SortedSet
from collections import defaultdict

INF = 10**18
N = int(input())
X = list(map(int, input().split()))
# niv [位置] = 一番近い距離
niv = defaultdict(lambda: INF)
data = SortedSet()
data.add(0)
ans = 0
for x in X:
    data.add(x)
    idx = data.bisect_left(x)
    # print("idx", idx)
    # 左側の人は絶対居る
    d1 = abs(data[idx] - data[idx-1])
    # 左側人の一番近い距離
    if d1 < niv[data[idx-1]]:
        if niv[data[idx-1]] < INF:
            ans -= niv[data[idx-1]]
        ans += d1
        niv[data[idx-1]] = d1
    # 右側の人はいるかわからないので無限遠点を基準とする
    d2 = INF
    if idx + 1 < len(data):
        d2 = abs(data[idx] - data[idx + 1])
        # 右側人の一番近い距離更新
        if d2 < niv[data[idx+1]]:
            # 無限遠でなければ現在のansから引く
            if niv[data[idx+1]] < INF:
                # print("Debug", x, niv[data[idx+1]], idx+1, data, len(data))
                ans -= niv[data[idx+1]]
            niv[data[idx+1]] = d2
            ans += d2

    # 左側の人が一番近い場合
    if d1 < d2:
        ans += d1
        niv[x] = d1
    else:
        ans += d2
        niv[x] = d2
    print(ans)
    # print(niv)
