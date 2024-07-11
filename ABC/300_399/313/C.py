N = int(input())
A = [int(l) for l in input().split()]
SA = sum(A)
TSA = SA // N
DSA = SA % N
if N - DSA < DSA:
    TSA += 1
PA = 0
PMA = 0
MA = 0
MMA = 0
for a in A:
    if a >= TSA:
        PA += a - TSA
        if PMA < a - TSA:
            PMA = a - TSA
    else:
        MA += TSA - a
        if MMA < TSA - a:
            MMA = TSA - a
M = min([PA, MA])
if M < PMA:
    print(M + (PMA - M) // 2)
if M < MMA:
    print(M + (MMA - M) // 2)
else:
    print(M)
