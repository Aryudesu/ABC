N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    tmp = data.get(a, 0)
    data[a] = tmp + 1
result = 0
for k in data:
    result += data.get(k, 0)//2
print(result)
