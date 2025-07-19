from sortedcontainers import SortedList

N, M = [int(l) for l in input().split()]
X = SortedList([int(l) for l in input().split()])
Y = SortedList()
result = 0
for i in range(len(X) - 1):
    Y.add(X[i+1] - X[i])
result = 0
while len(Y) + 1 > M:
    result += Y.pop(0)
print(result)
