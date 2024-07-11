def calc(H, W, S, K):
    # (縦に並んだ数, 縦の手数)
    dp = []
    # いくつ石が連なっているか
    wlen = 0
    # いくつ石を置いたか
    wc = 0
    # K <= max(H, W)なのでとりあえず超えるやつ
    result = H + W
    for w in range(W):
        if S[0][w] == ".":
            # K未満なら石を置く
            if wlen < K:
                wlen += 1
                wc += 1
            dp.append((1, 1))
        elif S[0][w] == "o":
            # 既にK以上なら手数は減る
            if wlen >= K:
                wc = max(0, wc - 1)
            # 連なっている石の個数を更新
            else:
                wlen += 1
            dp.append((1, 0))
        else:
            # 石の連なりは消えるし手数もリセット
            wlen = 0
            wc = 0
            dp.append((0, 0))
        if wlen >= K:
            result = min(result, wc)
    print(dp)
    for h in range(1, H):
        new_dp = []
        wlen = 0
        wc = 0
        for w in range(W):
            ylen, yc = dp[w]
            if S[h][w] == ".":
                # 連なりがK以下なら石を置く
                if ylen < K:
                    yc += 1
                    ylen += 1
                if wlen < K:
                    wc += 1
                    wlen += 1
                new_dp.append((ylen, yc))
            elif S[h][w] == "o":
                if ylen >= K:
                    yc = max(0, yc - 1)
                else:
                    ylen += 1
                if wlen >= K:
                    wc = max(0, wc - 1)
                else:
                    wlen += 1
                new_dp.append((ylen, yc))
            else:
                wc = 0
                wlen = 0
                new_dp.append((0, 0))
            if ylen >= K:
                result = min(result, yc)
            if wlen >= K:
                result = min(result, wc)
        dp = new_dp
        print(dp)
    return -1 if result == H + W else result



H, W, K = [int(l) for l in input().split()]
S = []
for h in range(H):
    S.append(input())

print(calc(H, W, S, K))
