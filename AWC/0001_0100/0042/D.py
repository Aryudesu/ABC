from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
data = defaultdict(int)
S = []
s = 0
for a in A:
    s = (s + a)%K
    S.append(s)
    data[s] += 1
# print(data)
result = 0
base = 0
for s in S:
    t = (K-base) % K
    if t in data:
        result += data[t]
    # print("debug", base, t, data[t])
    base = (base - (base + s)) % K
    # print(data)
    data[s] -= 1
print(result)
# 1 0 0 1 0
# - 2 2 0 2
# - - 0 1 0
# - - - 1 0
# - - - - 2