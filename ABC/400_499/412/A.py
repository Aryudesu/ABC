N = int(input())
res = 0
for n in range(N):
    a, b = [int(l) for l in input().split()]
    if a < b:
        res += 1
print(res)
