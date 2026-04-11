from sortedcontainers import SortedList

Q = int(input())
data = SortedList()
result = []
minus = 0
for _ in range(Q):
    n, h = map(int, input().split())
    if n == 1:
        data.add(h)
    elif n == 2:
        minus = data.bisect_right(h)
    else:
        raise ValueError()
    result.append(len(data) - minus)
for r in result:
    print(r)
