N, K = map(int, input().split())
A = list(map(int, input().split()))
S = []
s = 0
for a in A:
    s = (s + a) % K
    S.append(s)
# print(S)
data = {0}
result = 0
for s in S:
    if not data:
        data.add(s)
        continue
    if s in data:
        result += 1
        data = {s}
    else:
        data.add(s)
print(result)
