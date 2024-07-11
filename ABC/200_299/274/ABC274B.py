H, W = [int(l) for l in input().split()]
res = [0] * W
for h in range(H):
    C = input()
    for w in range(W):
        if C[w] == '#':
            res[w] += 1
print(*res)
