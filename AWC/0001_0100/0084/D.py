def isOk(N: int, num: int):
    p = None
    c = 0
    for i in range(N):
        b = num&1
        if p == b:
            c += 1
            if c == 3:
                return False
        else:
            c = 1
            p = b
        num >>= 1
    return True

INF = 1 << 30
N = int(input())
memo = set()
S = input()
T = input()
now = 0
for s in S:
    now = now * 2 + int(s)
tNum = 0
for t in T:
    tNum = tNum * 2 + int(t)
if now == tNum:
    print(0)
    exit(0)
memo.add(now)
result = 0
while True:
    result += 1
    okF = False
    nextNum = INF
    for i in range(N):
        b = 1 << i
        b2 = now & b
        if b2:
            nxt = now ^ b
            if isOk(N, nxt) and nxt not in memo:
                nextNum = min(nextNum, nxt)
                okF = True
        else:
            nxt = now | b
            if isOk(N, nxt) and nxt not in memo:
                nextNum = min(nextNum, nxt)
                okF = True
    if nextNum == tNum:
        break
    if not okF:
        result = -1
        break
    memo.add(nextNum)
    now = nextNum
print(result)
