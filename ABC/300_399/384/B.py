N, R = [int(l) for l in input().split()]

for n in range(N):
    d, a = [int(l) for l in input().split()]
    if d == 1 and 1600 <= R and R <= 2799:
        R += a
    if d == 2 and 1200 <= R and R <= 2399:
        R += a
print(R)
