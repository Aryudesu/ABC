from collections import defaultdict
data = defaultdict(int)
S = input()
m = 0
for s in S:
    data[s] += 1
    m = max(m, data[s])
C = set()
for s in data:
    if data[s] == m:
        C.add(s)
result = ""
for s in S:
    if s in C:
        continue
    result += s
print(result)
