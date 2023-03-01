import math

N = int(input())
result = []
m = int(math.sqrt(N))
if m*m == N:
    pass
elif (m+1)**2 == N:
    m = m + 1
for n in range(1, m + 1):
    if N % n == 0:
        result.append(n)
        if N // n != n:
            result.append(N//n)
for r in result:
    print(r)
