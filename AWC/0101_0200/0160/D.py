from collections import defaultdict
from sortedcontainers import SortedList

INF = 10 ** 18
N, Q = map(int, input().split())
A = list(map(int, input().split()))
data = SortedList(A)
for _ in range(Q):
    t, x, r = map(int, input().split())
    if r == 1:
        continue
    match t:
        case 1:
            num = data.pop()
            data.add(x)
        case 2:
            num = data.pop(0)
            data.add(x)
        case _:
            raise ValueError()
print(sum(data))
