from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
data = defaultdict(int)
result = 0
for a in A:
    result += data[a%100]
    data[(100-a)%100] += 1
print(result)
