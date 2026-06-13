from collections import defaultdict
N, M = map(int, input().split())
T = list(map(int, input().split()))
SC = defaultdict(lambda: 10000000000)
for m in range(M):
    s, c = map(int, input().split())
    SC[s] = min(SC[s], c)
result = 0
for t in T:
    if t not in SC:
        result = -1
        break
    result += SC[t]
print(result)
