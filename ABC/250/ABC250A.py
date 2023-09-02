H, W = [int(l) for l in input().split()]
R, C = [int(l) for l in input().split()]

res = 0
if R - 1 >= 1:
    res += 1
if R + 1 <= H:
    res += 1
if C - 1 >= 1:
    res += 1
if C + 1 <= W:
    res += 1

print(res)
