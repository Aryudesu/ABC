N = int(input())
A = [int(l) for l in input().split()]
count = dict()
for a in A:
    count[a] = count.get(a, 0) + 1
print(count.get(100, 0) * count.get(400, 0) +
      count.get(200, 0) * count.get(300, 0))
