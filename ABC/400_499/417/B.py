from collections import defaultdict

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
Bdata = defaultdict(lambda:0)
for b in B:
    Bdata[b] += 1
# print(Bdata)
result = []
for a in A:
    if Bdata[a] > 0:
        Bdata[a] -= 1
    else:
        result.append(a)
print(*result)
