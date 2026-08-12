from bisect import bisect_left
import sys
sys.setrecursionlimit(10**6)


def getLca(P: list[int], u: int, v: int)->int:
    nowU = u
    nowV = v
    while nowU != nowV:
        if nowU < nowV:
            nowV = P[nowV]
        else:
            nowU = P[nowU]
    return nowU

def lisLength(A: list[int]):
    dp = []
    for a in A:
        i = bisect_left(dp, a)
        if i == len(dp):
            dp.append(a)
        else:
            dp[i] = a
    return len(dp)

def getPath(P: list[int], u: int, v: int, lca: int)->list[int]:
    uPath = []
    vPath = []
    nowU = u
    while nowU != lca:
        uPath.append(nowU)
        nowU = P[nowU]
    nowV = v
    while nowV != lca:
        vPath.append(nowV)
        nowV = P[nowV]
    vPath.reverse()
    return uPath + [lca] + vPath

N, Q = map(int, input().split())
H = list(map(int, input().split()))
if N > 1:
    P = [-1] + [int(l) - 1 for l in input().split()]
else:
    input()
    for _ in range(Q):
        u, v = map(int, input().split())
        print(1)
    exit(0)

result = []
memo = dict()
for _ in range(Q):
    u, v = map(int, input().split())
    key = (u-1, v-1)
    if key in memo:
        result.append(memo[key])
        continue
    lca = getLca(P, u-1, v-1)
    path = getPath(P, u-1, v-1, lca)
    path.reverse()
    pathH = [H[p] for p in path]
    res = lisLength(pathH)
    result.append(res)
    memo[key] = res
print(*result, sep="\n")
