N = int(input())
A = [int(l) for l in input().split()]
B = [10 ** len(str(a)) for a in A]
C = []
r = 0
MOD = 998244353
for n in range(N):
    r += B[-n - 1]
    C.append(r)
C.reverse()
result = 0
for n in range(N):
    result = (result + A[n] * (C[n] - B[n] + n)) % MOD
print(result)
