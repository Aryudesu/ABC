from sortedcontainers import SortedList

X = int(input())
Q = int(input())
data = SortedList()
data.add(X)
result = []
for q in range(Q):
    a, b = map(int, input().split())
    data.add(a)
    data.add(b)
    result.append(data[q + 1])
for r in result:
    print(r)
