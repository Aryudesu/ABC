import math

N = int(input())
x = [int(l) for l in input().split()]
man = 0
euc = 0
cheb = 0
for n in range(N):
    man += abs(x[n])
    euc += x[n] * x[n]
    if cheb < abs(x[n]):
        cheb = abs(x[n])

print(man)
print(math.sqrt(euc))
print(cheb)
