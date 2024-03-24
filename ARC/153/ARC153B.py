H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append(list(input()))
Q = int(input())
HS = 0
WS = 0
for q in range(Q):
    a, b = [int(l) for l in input().split()]
    if q % 2:
        HS = (1 - a + HS + H) % H
        WS = (1 - b + WS + W) % W
    else:
        HS = (a - 1 + HS + H) % H
        WS = (b - 1 + WS + W) % W
    # print(HS)
    # print(WS)
if Q % 2:
    for h in range(H):
        for w in range(W):
            print(A[(HS - h) % H][(WS - w) % W], end="")
        print()
else:
    for h in range(H):
        for w in range(W):
            print(A[(HS + h) % H][(WS + w) % W], end="")
        print()
