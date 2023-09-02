H, W = [int(l) for l in input().split()]
result = []
Alp = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for h in range(H):
    result.append("".join([Alp[int(l)] for l in input().split()]))
for r in result:
    print(r)
