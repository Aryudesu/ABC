N, H, X = [int(l) for l in input().split()]
P = [int(l) for l in input().split()]
result = 0
for p in P:
    if H + p >= X:
        break
    result += 1
print(result + 1)
