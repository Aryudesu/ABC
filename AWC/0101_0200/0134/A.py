from collections import defaultdict
N = int(input())
cData = defaultdict(list)
for n in range(N):
    c, l = map(int, input().split())
    cData[c].append(l)
result = 0
for c, vals in cData.items():
    for i in range(len(vals) - 1):
        for j in range(i + 1, len(vals)):
            result += abs(vals[i] - vals[j])
print(result)
