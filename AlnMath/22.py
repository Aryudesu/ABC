import math

N = int(input())
A = [int(l) for l in input().split()]
data = dict()
for a in A:
    data[a] = data.get(a, 0) + 1
result = 0
for idx in range(N//2):
    tmp = 100000 - A[idx]
    if tmp != A[idx]:
        result += data.get(A[idx], 0) * data.get(100000 - A[idx], 0)
n = data.get(50000, 0)
r = 2
if n >= 2:
    result += math.factorial(math.factorial(n) //
                             (math.factorial(r) * math.factorial(n-r)))
print(result)
