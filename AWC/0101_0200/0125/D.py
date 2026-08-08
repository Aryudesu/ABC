from collections import deque

N, D = map(int, input().split())
plus = []
minus = []
for n in range(N):
    c, p = map(int, input().split())
    if p-c > 0:
        plus.append((p, p-c))
    else:
        minus.append((p-c))

if not plus:
    minus.sort()
    print(minus[-1])
    exit(0)

plus.sort()
data = deque()
s = 0
result = 0
L = len(plus)
for r in range(L):
    p = plus[r]
    data.append(p)
    s += p[1]
    while data and data[-1][0] - data[0][0] > D:
        q = data.popleft()
        s -= q[1]
    # print(data)
    result = max(s, result)
print(result)
