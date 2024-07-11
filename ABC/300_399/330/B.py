N, L, R = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = []
for a in A:
    if a <= L:
        result.append(L)
    elif a >= R:
        result.append(R)
    else:
        result.append(a)
print(*result)
