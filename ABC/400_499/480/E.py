from math import isqrt

# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

def isOk(M: int, N: int, L: int, D: int)->bool:
    if D == 0:
        return False
    res = 1
    for l in range(0, L):
        res *= (N + l * D)
        if res > M:
            return False
    return res <= M

def searchIdx(M: int, L: int, D: int)->int:
    if not isOk(M, 1, L, D):
        return -1
    l = 0
    r = M + 1
    while r - l > 1:
        mid = (r + l) // 2
        if isOk(M, mid, L, D):
            l = mid
        else:
            r = mid
    return l

M = int(input())
# 10^18 のとき19!がせいぜい -> 長さ20くらいで打ち切っても良いかも
result = 0
for L in range(3, 20):
    check = searchIdx(M, L, 1)
    if check <= 0:
        break
    result += check
    # 長さLのときの{}_k P_ Lのkを求めたい
    prev = 2
    for D in range(prev, M + 1):
        if D * D > M:
            break
        start = searchIdx(M, L, D)
        if start <= 0:
            break
        result += start
        prev = D
print(result)
# なんか色々奇跡的なことあって通ってくれ
