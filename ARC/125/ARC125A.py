N, M = [int(l) for l in input().split()]
S = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]

S0F = False
S1F = False
T0F = False
T1F = False
for s in S:
    if s:
        S1F = True
    else:
        S0F = True

