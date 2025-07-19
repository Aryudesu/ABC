# なんでWA出てるのわからん助けて　なんかの間違いで通ってくれ(´；ω；｀)ﾌﾞﾜｯ
N, Q = [int(l) for l in input().split()]
# 方針：最後にサーバ名に影響を与えたPCを追う
QUERY = []
for _ in range(Q):
    query = input().split()
    q = int(query[0])
    if q == 1:
        p = int(query[1])
        QUERY.append((q, p))
    elif q == 2:
        p, s = int(query[1]), query[2]
        QUERY.append((q, p, s))
    elif q == 3:
        p = int(query[1])
        QUERY.append((q, p))

# クエリ逆読み
QUERY.reverse()
result = []
# サーバに最後に影響を与えたPC
pc = 0
for query in QUERY:
    if query[0] == 1:
        n, p = query
        # pはサーバから受け取ったので，次にサーバに影響を与えるPCを見つけるまで保留
        # pの追跡を解除する
        if pc == p:
            pc = 0
    elif query[0] == 2:
        n, p, s = query
        # 最後にサーバ名に影響を与えたPCであれば文字列を追加
        if pc == p:
            result.append(s)
    elif query[0] == 3:
        # 最後にサーバ名に影響を与えたPCなので保持
        n, p = query
        # 今度はこいつを追跡する
        if pc == 0:
            pc = p
# 出力
result.reverse()
print(*result, sep="")
