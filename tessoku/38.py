D, N = [int(l) for l in input().split()]
data = [24] * (D + 1)
data[0] = 0
for n in range(N):
    L, R, H = [int(l) for l in input().split()]
    for d in range(L, R + 1):
        if d > D:
            break
        data[d] = min(data[d], H)
# print(data)
print(sum(data))
