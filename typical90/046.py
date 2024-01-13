N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
C = [int(l) for l in input().split()]
D = 46
dataA = dict()
dataB = dict()
dataC = dict()
for a in A:
    key = a % D
    dataA[key] = dataA.get(key, 0) + 1
for b in B:
    key = b % D
    dataB[key] = dataB.get(key, 0) + 1
for c in C:
    key = c % D
    dataC[key] = dataC.get(key, 0) + 1
result = 0
for a in dataA:
    for b in dataB:
        c = (- a - b) % D
        itemA = dataA.get(a, 0)
        itemB = dataB.get(b, 0)
        itemC = dataC.get(c, 0)
        result += itemA * itemB * itemC
print(result)
