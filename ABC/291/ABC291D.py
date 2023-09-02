N = int(input())
AB = []
for n in range(N):
    AB.append([int(l) for l in input().split()])
MOD = 998244353
resultA = 1
resultB = 1
for i in range(1, N):
    new_resultA = 0
    new_resultB = 0
    pab = AB[i-1]
    ab = AB[i]
    if ab[0] != pab[0]:
        new_resultA = (new_resultA + resultA) % MOD
    if ab[0] != pab[1]:
        new_resultA = (new_resultA + resultB) % MOD
    if ab[1] != pab[0]:
        new_resultB = (new_resultB + resultA) % MOD
    if ab[1] != pab[1]:
        new_resultB = (new_resultB + resultB) % MOD
    resultA = new_resultA
    resultB = new_resultB
print((resultA + resultB) % MOD)
