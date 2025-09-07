from sortedcontainers import SortedList

Q = int(input())
result = []
data = SortedList()
for _ in range(Q):
    query = [int(l) for l in input().split()]
    if query[0] == 1:
        data.add(query[1])
    elif query[0] == 2:
        result.append(data.pop(0))

for r in result:
    print(r)
