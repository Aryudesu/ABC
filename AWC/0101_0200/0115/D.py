from typing import Tuple
INF = 10 ** 18

def calcLength(T: int, XVL: list[Tuple[int, int, int]])->int:
    M = -INF
    m = INF
    for x, v, l in XVL:
        M = max(M, x + v * T + l)
        m = min(m, x + v * T - l)
    return M - m

def check(T: int, XVL: list[Tuple[int, int, int]])->bool:
    return calcLength(T+1, XVL) < calcLength(T, XVL)

def calc(XVL: list[Tuple[int, int, int]], L: int, R: int)->int:
    l = L - 1
    r = R
    while r - l > 1:
        mid = (r + l) // 2
        if check(mid, XVL):
            l = mid
        else:
            r = mid
    return calcLength(r, XVL)


N, D, Q = map(int, input().split())
XVL = []
for _ in range(N):
    x, v, l = map(int, input().split())
    XVL.append((x, v, l))

result = [calc(XVL, 0, D)]
for _ in range(Q):
    p, a, b, c = map(int, input().split())
    XVL[p-1] = (a, b, c)
    result.append(calc(XVL, 0, D))
for res in result:
    print(res)
