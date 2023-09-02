N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
Mem = []
prev = 0
for a in A:
    tmp = a - prev
    Mem.append(tmp)
    prev = a
Q = int(input())
result = []
for q in range(Q):
    l, r = [int(l) - 1 for l in input().split()]
    res = True
    for k in range(K - 1):
        lnum = Mem[r - k - K] if l < r - k - K else 0
        tmp = Mem[r - k] + lnum
        if tmp:
            res = False
            break
    result.append("Yes" if res else "No")
for r in result:
    print(r)
