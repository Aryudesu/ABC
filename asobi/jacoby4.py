N = int(input())
P = [int(l) for l in input().split()]
data = dict()
for p in P:
    tmp = data.get(p, 1)
    if p == 2 and tmp != 1:
        continue
    data[p] = tmp * p + 1
result = 1
for p in data:
    result *= data.get(p, 1)
print(8 * result)
