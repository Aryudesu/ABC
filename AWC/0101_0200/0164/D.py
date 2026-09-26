from typing import Tuple
# 無理だああああああ助けて
def mergeIntervals(data: list[Tuple[int, int]])-> list[Tuple[int, int]]:
    """半開区間[L, R)の範囲結合を行います．"""
    if len(data) == 0:
        return []
    data.sort()
    result = [data[0]]
    for l, r in data[1:]:
        pl, pr = result[-1]
        if l <= pr:
            result[-1] = (pl, max(pr, r))
        else:
            result.append((l, r))
    return result

# この条件で達成可能か
def isOk(T: int, K: int, M: int, LR: list[Tuple[int, int]])->bool:
    # 次の工事開始地点
    nextStart = 0
    # 前のループで塗ったか
    prev = False
    for l, r in mergeIntervals(LR):
        # 次の開始地点からK伸ばす必要がある
        if l - nextStart < K:
            # Mの間隔まで開けられるが回避することができない
            if r - nextStart > M:
                return False
            if not prev:
                return False
            nextStart = r
            prev = False
        else:
            # 開始地点からK超過までの距離があればそれまで区間を伸ばせる
            if r - l > M:
                return False
            nextStart = r
            prev = True
    return (T - nextStart >= K) or (prev and T - nextStart <= M)



T, N, K, M = map(int, input().split())
result = 0
LR = []
for _ in range(N):
    l, r = map(int, input().split())
    LR.append((l, r))
LR.sort()
# 重なっても良いものを1とする
result = N
for mask in range(1 << N):
    data = []
    for n in range(N):
        b = 1 << n
        if mask & b:
            continue
        data.append(LR[n])
    if isOk(T, K, M, data):
        result = min(result, mask.bit_count())
print(result)
