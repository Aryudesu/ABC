N, C = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
s = sum(A)
dataA = 0
dataB = 0
M = 0
if C > 0:
    for a in A:
        dataA += a
        if dataA < 0:
            dataA = 0
        if M < dataA:
            M = dataA
    print((s-M) + C * M)
elif C <= 0:
    for a in A:
        dataA += a
        if dataA > 0:
            dataA = 0
        if M > dataA:
            M = dataA
    print((s-M) + C * M)
