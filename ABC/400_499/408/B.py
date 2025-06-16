from sortedcontainers import SortedSet

N = int(input())
A = SortedSet([int(l) for l in input().split()])
result = []
for a in A:
    result.append(a)
print(len(result))
print(*result)
