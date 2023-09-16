C = [[int(l) for l in input().split()] for _ in range(3)]
data = dict()
dup = set()


# 事前データ作成 {パネル状態: {空いてたらガッカリするやつ}}
def calc_zizen_data(h, w, hh, ww):
    if w == ww and h == hh:
        return
    if C[h][w] != C[hh][ww]:
        return
    if h == hh:
        th = h
        tw = 3 - w - ww
    elif w == ww:
        th = 3 - h - hh
        tw = w
    elif h == w and hh == ww:
        th = 3 - h - hh
        tw = 3 - w - ww
    elif h == 2 - w and hh == 2 - ww:
        th = 3 - h - hh
        tw = 3 - w - ww
    else:
        return
    num = (1 << (h * 3 + w)) | (1 << (hh * 3 + ww))
    key = 1 << (th * 3 + tw)
    tmp = data.get(key, set())
    tmp.add(num)
    data[key] = tmp
    dup.add(num)


for w in range(3):
    for h in range(3):
        for ww in range(3):
            for hh in range(3):
                calc_zizen_data(h, w, hh, ww)

# bitDP : {パネル状態: ガッカリ回数}
bunbo = 1
for i in range(1, 10):
    bunbo *= i
dp = {0: 0}
# 9回埋めたら全通り
for _ in range(9):
    new_dp = dict()
    # 各パネル1個開ける
    for i in range(9):
        # 開ける位置
        k = 1 << i
        # 前まで開けてたやつ
        for key in dp:
            # すでに開けてたらスルー
            if key & k:
                continue
            # そのパネル開けた時にすでに空いてたらガッカリする組み合わせ一覧
            sdata = data.get(k, set())
            count = 0
            for sd in sdata:
                # すでに2つが空いてたら
                if key & sd == sd:
                    count += 1
            new_dp[key | k] = dp[key] + new_dp.get(key | k, 0) + count
    dp = new_dp
print(dp.get(511)/bunbo)
