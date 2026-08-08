from collections import defaultdict
N, M, T = map(int, input().split())
CS = defaultdict(int)
CC = [0] * (N + 1)
ss = 0
for m in range(M):
    c, s = map(int, input().split())
    CS[c] += s
    CC[c] += 1
result = 0
for c in CS:
    ss = CS[c]
    cc = CC[c]
    if ss < T * cc:
        result += 1
print(result)
