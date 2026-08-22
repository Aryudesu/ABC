from sortedcontainers import SortedSet

N = int(input())
H = list(map(int, input().split()))
INF = 10 ** 30
firstIdx = None
secondIdx = None
if len(H) > 1:
    if H[0] >= H[1]:
        firstIdx = 0
        secondIdx = 1
    else:
        firstIdx = 1
        secondIdx = 0
