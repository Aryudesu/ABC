from sortedcontainers import SortedSet

INF = 10**18
N = int(input())
A = SortedSet(map(int, input().split()))
A.add(-INF)
A.add(INF)
result = 0
now = 0
while len(A) > 2:
    nowIdx = A.bisect_right(now)
    r = A.pop(nowIdx)
    l = A.pop(nowIdx-1)
    if abs(now - l) <= abs(now - r):
        A.add(r)
        result += abs(now - l)
        now = l
    else:
        A.add(l)
        result += abs(now - r)
        now = r
    # print(A)
    # print(l, r)
    # print(nowIdx)
print(result)
