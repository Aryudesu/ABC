from collections import defaultdict

N = int(input())
A = [int(l) for l in input().split()]
data = defaultdict(int)
for a in A:
    data[a] += 1
result = 0
for k in data:
    kNum = data[k]
    tmp = kNum * (kNum - 1) // 2
    result += tmp * (N - kNum)
print(result)
