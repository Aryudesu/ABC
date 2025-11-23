from sortedcontainers import SortedList
from collections import deque

Q = int(input())
data = deque()
sortedData = SortedList()
result = []
for _ in range(Q):
    query = list(map(int, input().split()))
    n = query[0]
    if n == 1:
        x = query[1]
        data.append(x)
    elif n == 2:
        num = 0
        if len(sortedData) > 0:
            num = sortedData.pop(0)
        else:
            num = data.popleft()
        result.append(num)
    elif n == 3:
        for num in data:
            sortedData.add(num)
        data = deque()
    else:
        raise Exception()
for r in result:
    print(r)
