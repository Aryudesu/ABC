M, D = [int(l) for l in input().split()]
y, m, d = [int(l) for l in input().split()]
ny, nm, nd = y, m, d
nd += 1
if D + 1 == nd:
    nd = 1
    nm += 1
    if M + 1 == nm:
        ny += 1
        nm = 1
print(ny, nm, nd)