H, W = [int(l) for l in input().split()]
count = 0
for h in range(H):
    S = input()
    for s in S:
        if s == '#':
            count += 1
print(count)
