N, L, R = [int(l) for l in input().split()]
count = 0
for n in range(N):
    l, r = [int(l) for l in input().split()]
    if l <= L and R <= r:
        count += 1
print(count)
