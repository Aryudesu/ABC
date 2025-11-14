from collections import defaultdict

N = int(input())
WHB = [list(map(int, input().split())) for _ in range(N)]
# (体の重さ - 頭の重さ) = 嬉しさ
# 正になるのが好ましい
dpData = defaultdict(int)
dpData[0] = 0
# 身体に残り全部使った場合の総和
maxW = 0
for w, h, b in WHB:
    maxW += w
WHB.sort(reverse=True)

result = 0
for w, h, b in WHB:
    nextDpData = defaultdict(int)
    # 残りの重さから今回の重さを引いておく
    maxW -= w
    for key in dpData:
        # 現在の身体の重さと頭の重さの差
        hbw = key
        nowV = dpData[key]
        # 頭に使って今後大丈夫な場合は考慮する
        if hbw - w + maxW >= 0:
            # 頭に取り付けた場合の嬉しさ
            tmp = max(dpData[key] + h, nextDpData[hbw - w])
            if hbw - w >= 0:
                result = max(result, tmp)
            nextDpData[hbw - w] = tmp
        # 体に取り付けた場合の嬉しさ
        tmp = max(dpData[key] + b, nextDpData[hbw + w])
        if hbw + w >= 0:
            result = max(result, tmp)
        nextDpData[hbw + w] = tmp
    dpData = nextDpData
print(result)
