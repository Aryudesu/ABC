from collections import defaultdict

S = input()
data = defaultdict(int)
for s in S:
    data[s] += 1
for k in data:
    if data[k] == 1:
        print(k)
