# 黒にした場合
def toBlack(N, A, idx):
    # 真ん中で両側が白はカウント増える
    if idx - 1 >= 0 and idx + 1 < N:
        if not A[idx-1] and not A[idx + 1]:
            return 1
        # 真ん中で両側が黒はカウント減る
        if A[idx-1] and A[idx + 1]:
            return -1
    # 左端で右側が白はカウント増える
    if idx - 1 < 0 and idx + 1 < N:
        if not A[idx + 1]:
            return 1
    # 右端で左側が白はカウント増える
    if idx - 1 >= 0 and idx + 1 >= N:
        if not A[idx - 1]:
            return 1
    # 1マスの場合はカウント増える
    if N == 1:
        return 1
    return 0

# 白にした場合
def toWhite(N, A, idx):
    # 真ん中で両側が黒はカウント増える
    if idx - 1 >= 0 and idx + 1 < N:
        if A[idx-1] and A[idx + 1]:
            return 1
        # 真ん中で両側が白はカウント減る
        if not A[idx-1] and not A[idx + 1]:
            return -1
    # 左端で右側が白はカウント減る
    if idx - 1 < 0 and idx + 1 < N:
        if not A[idx + 1]:
            return -1
    # 右端で左側が白はカウント増える
    if idx - 1 >= 0 and idx + 1 >= N:
        if not A[idx - 1]:
            return -1
    # 1マスの場合はカウント減る
    if N == 1:
        return -1
    # その他の場合はカウント変化なし
    return 0


N, Q = [int(l) for l in input().split()]
A = [int(l) - 1 for l in input().split()]
data = [False] * N

count = 0
for a in A:
    data[a] = not data[a]
    if data[a]:
        count += toBlack(N, data, a)
    else:
        count += toWhite(N, data, a)
    # print(data)
    print(count)

