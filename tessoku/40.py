N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    data[a] = data.get(a, 0) + 1
result = 0
for key in data:
    num = data.get(key, 0)
    if num >= 3:
        result += (num * (num - 1) * (num - 2)) // 6
print(result)
