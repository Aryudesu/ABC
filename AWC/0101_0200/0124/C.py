def isOk(mid: int, R: list[int], M: int)->bool:
    """更に減らすことが可能か"""
    result = 0
    for r in R:
        # 入れるコマ数
        result += max(0, r - mid)
    # print(mid)
    # 減らす余裕があるか
    return result <= M
    

N, M = map(int, input().split())
R = list(map(int, input().split()))
if sum(R) < M:
    print(-1)
    exit(0)
l, r = -1, max(R) + 1
while r - l > 1:
    mid = (r + l) // 2
    if isOk(mid, R, M):
        r = mid
    else:
        l = mid
print(r)
