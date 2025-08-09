from sortedcontainers import SortedList

data1 = SortedList()
Q = int(input())
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        n, x = query
        data1.add(x)
    elif query[0] == 2:
        print(data1[0])
    elif query[0] == 3:
        data1.pop(0)
