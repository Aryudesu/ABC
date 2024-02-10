import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

INF = 10**18
N = int(input())
S = [input() for _ in range(N)]
memo = [False] * (N ** 4 + 1)
resmemo = [INF + 1] * (N ** 4 + 1)


def ept(c):
    return c == "." or c == "P"

def conv2yx(p1y, p1x, p2y, p2x):
    return p1y * (N * N * N) + p1x * (N * N) + p2y * N + p2x

def searchResult(depth, num):
    if resmemo[num] != INF + 1:
        return resmemo[num]
    result = INF
    p1, p2 = num // (N * N), num % (N * N)
    p1y, p1x = p1 // N, p1 % N
    p2y, p2x = p2 // N, p2 % N
    tp1y, tp1x, tp2y, tp2x = p1y, p1x, p2y, p2x
    if p1y - 1 >= 0 and ept(S[p1y-1][p1x]):
        tp1y -= 1
    if p2y - 1 >= 0 and ept(S[p2y-1][p2x]):
        tp2y -= 1
    if p1y != tp1y or p2y != tp2y:
        if tp1y == tp2y and tp1x == tp2x:
            return depth
        tmp = conv2yx(tp1y, tp1x, tp2y, tp2x)
        if not memo[tmp]:
            memo[tmp] = True
            res = searchResult(depth + 1, tmp)
            memo[tmp] = False
            if res < result:
                result = res
            if resmemo[num] > res:
                resmemo[num] = (res, depth)

    tp1y, tp1x, tp2y, tp2x = p1y, p1x, p2y, p2x
    if p1y + 1 < N and ept(S[p1y+1][p1x]):
        tp1y += 1
    if p2y + 1 < N and ept(S[p2y+1][p2x]):
        tp2y += 1
    if p1y != tp1y or p2y != tp2y:
        if tp1y == tp2y and tp1x == tp2x:
            return depth
        tmp = conv2yx(tp1y, tp1x, tp2y, tp2x)
        if not memo[tmp]:
            memo[tmp] = True
            res = searchResult(depth + 1, tmp)
            memo[tmp] = False
            if res < result:
                result = res
            if resmemo[num] > res:
                resmemo[num] = (res, depth)

    tp1y, tp1x, tp2y, tp2x = p1y, p1x, p2y, p2x
    if p1x - 1 >= 0 and ept(S[p1y][p1x-1]):
        tp1x -= 1
    if p2x - 1 >= 0 and ept(S[p2y][p2x-1]):
        tp2x -= 1
    if p1x != tp1x or p2x != tp2x:
        if tp1y == tp2y and tp1x == tp2x:
            return depth
        tmp = conv2yx(tp1y, tp1x, tp2y, tp2x)
        if not memo[tmp]:
            memo[tmp] = True
            res = searchResult(depth + 1, tmp)
            memo[tmp] = False
            if res < result:
                result = res
            if resmemo[num] > res:
                resmemo[num] = (res, depth)

    tp1y, tp1x, tp2y, tp2x = p1y, p1x, p2y, p2x
    if p1x + 1 < N and ept(S[p1y][p1x+1]):
        tp1x += 1
    if p2x + 1 < N and ept(S[p2y][p2x+1]):
        tp2x += 1
    if p1x != tp1x or p2x != tp2x:
        if tp1y == tp2y and tp1x == tp2x:
            return depth
        tmp = conv2yx(tp1y, tp1x, tp2y, tp2x)
        if not memo[tmp]:
            memo[tmp] = True
            res = searchResult(depth + 1, tmp)
            memo[tmp] = False
            if res < result:
                result = res
            if resmemo[num] > res:
                resmemo[num] = (res, depth)
    if resmemo[num] > result:
        resmemo[num] = (result, depth)
    return result

p1 = None
p2 = None
for n in range(N):
    for m in range(N):
        tmp = n * N + m
        if S[n][m] == "P" and p1 is None:
            p1 = n * N + m
        elif S[n][m] == "P":
            p2 = n * N + m
result = searchResult(1, p1 * N * N + p2)
print(-1 if result == INF else result)
