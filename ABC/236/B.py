N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    data[a] = data.get(a, 0) + 1
for k in data:
    if data.get(k, 0) == 3:
        print(k)
        break
