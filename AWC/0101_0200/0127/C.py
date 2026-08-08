def isOk(A: list[int], mid: int, M: int)->bool:
    count = 1
    weight = 0
    for a in A:
        if a > mid:
            return False
        if weight + a <= mid:
            weight += a
        else:
            # 次のトラック
            weight = a
            count += 1
    return count <= M

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = sum(A)
while r - l > 1:
    mid = (r + l) // 2
    # 積載量の最大値を減らすことができるか
    if isOk(A, mid, M):
        r = mid
    else:
        l = mid
    # print(r, l)
# print(l, r)
print("Yes" if r > K else "No")
