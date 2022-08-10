MOD= 10**9 + 7
N = int(input())
A = [int(l) % MOD for l in input().split()]
S = [0]*N
s = 0

for i in range(1, N+1):
    s = (s + A[-i])%MOD
    S[-i] = s

res = 0
for i in range(N-1):
    res = (res + A[i]*S[i+1])%MOD
print(res)
