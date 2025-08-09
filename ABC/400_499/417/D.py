MAX = 10
N = int(input())
PAB = []
pad = []
pd = 0
for n in range(N):
    p, a, b = [int(l) for l in input().split()]
    pad.append(p + pd)
    pd += b
    PAB.append([p, a, b])
print(pad)
data = []
for n in range(MAX):
    now = n
    memo = [now]
    for i in range(N):
        p, a, b = PAB[i]
        if now <= p:
            now += a
        else:
            now = max(0, now - b)
        memo.append(now)
    print(memo)
    for i in range(N + 1):
        if memo[i] < MAX:
            data[i][memo[i]] = now
for d in data:
    print(d)
result = []
Q = int(input())
for q in range(Q):
    X = int(input())
    # result.append(data[X])
for r in result:
    print(r)
