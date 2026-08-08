from collections import defaultdict

N = int(input())
data = defaultdict(lambda:defaultdict(int))
for n in range(N):
    p, q = map(int, input().split())
    data[p][q] += 1
result = 0
for p in data:
    s = 0
    res = 0
    for q in data[p]:
        res += s * data[p][q]
        s += data[p][q]
    result += res
print(result)
