import itertools

N = int(input())
X = [int(l) for l in input().split()]
minus = [l for l in X if l < 0]
plus = [l for l in X if l > 0]
minus.sort(reverse=True)
plus.sort(reverse=True)
X = minus + plus
if N < 6:
    A = X
else:
    A = [X[0], X[1], X[2], X[-3], X[-2], X[-1]]
result_M = -10**20
result_m = 10**20
for dat in itertools.permutations(A, 3):
    tmpa = dat[0] + dat[1] + dat[2]
    tmpb = dat[0] * dat[1] * dat[2]
    if result_M < tmpa/tmpb:
        result_M = tmpa/tmpb
    if result_m > tmpa/tmpb:
        result_m = tmpa/tmpb
print(result_m)
print(result_M)
