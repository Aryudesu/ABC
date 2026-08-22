from typing import Tuple

def calcP(N: int)->Tuple[dict[int, int], bool]:
    result = dict()
    if N == 0:
        return {2: 10000, 3: 10000, 5: 10000, 7: 10000}, True
    num = N
    for p in [2, 3, 5, 7]:
        while num % p == 0:
            result[p] = result.get(p, 0) + 1
            num //= p
    return result, num == 1

def makeNextKey(key: Tuple[int, int, int, int], goal: Tuple[int, int, int, int], num: int)->Tuple[int, int, int, int]:
    ni, san, go, nana = key
    nextKey = None
    if num == 1:
        nextKey = (ni, san, go, nana)
    elif num == 2:
        if ni + 1 > goal[0]:
            return None
        nextKey = (ni + 1, san, go, nana)
    elif num == 3:
        if san + 1 > goal[1]:
            return None
        nextKey = (ni, san + 1, go, nana)
    elif num == 4:
        if ni + 2 > goal[0]:
            return None
        nextKey = (ni + 2, san, go, nana)
    elif num == 5:
        if go + 1 > goal[2]:
            return None
        nextKey = (ni, san, go + 1, nana)
    elif num == 6:
        if ni + 1 > goal[0] or san + 1 > goal[1]:
            return None
        nextKey = (ni + 1, san + 1, go, nana)
    elif num == 7:
        if nana + 1 > goal[3]:
            return None
        nextKey = (ni, san, go, nana + 1)
    elif num == 8:
        if ni + 3 > goal[0]:
            return None
        nextKey = (ni + 3, san, go, nana)
    elif num == 9:
        if san + 2 > goal[1]:
            return None
        nextKey = (ni, san + 1, go, nana)
    return nextKey

def calcTimeK(N: str, kP: dict[int, int])->int:
    giri = dict()
    dp = dict()
    giri[(0, 0, 0, 0)] = 1
    dp[(0, 0, 0, 0)] = 1
    S = list(N)
    S.reverse()
    goal = (kP.get(2, 0), kP.get(3, 0), kP.get(5, 0), kP.get(7, 0))
    result = 0
    for s in S:
        m = int(s)
        nextGiri = dict()
        nextDP = dict()
        for key, value in giri.items():
            for j in range(0, m + 1):
                nextKey = makeNextKey(key, goal, j)
                if nextKey is None:
                    continue
                if j == m:
                    nextGiri[nextKey] = nextGiri.get(nextKey, 0) + value
                else:
                    nextDP[nextKey] = nextDP.get(nextKey, 0) + value
        for key, value in dp.items():
            for j in range(1, 10):
                nextKey = makeNextKey(key, goal, j)
                if nextKey is None:
                    continue
                nextDP[nextKey] = nextDP.get(nextKey, 0) + value
        giri, dp = nextGiri, nextDP

L, R, K = map(int, input().split())
kP, res = calcP(K)
if not res:
    print(0)
    exit(0)
calcTimeK(str(L), kP)
