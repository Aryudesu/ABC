N = int(input())
A = [int(l) for l in input().split()]
B = [a for a in A]
B = list(set(B))
B.sort()
data = dict()
for i in range(len(B)):
    data[B[i]] = i + 1
result = []
for a in A:
    result.append(data[a])
print(*result)
