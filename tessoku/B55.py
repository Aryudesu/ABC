from sortedcontainers import SortedSet

result = []
data = SortedSet()
Q = int(input())
for q in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        data.add(x)
    else:
        if len(data) == 0:
            result.append(-1)
            continue
        if x in data:
            result.append(0)
            continue
        idx = data.bisect_left(x)
        tmp1 = 10 ** 10
        if idx < len(data):
            tmp1 = min(tmp1, abs(data[idx] - x))
        if idx - 1 >= 0:
            tmp1 = min(tmp1, abs(data[idx-1] - x))
        result.append(tmp1)
for r in result:
    print(r)
