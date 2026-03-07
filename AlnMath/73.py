MOD = 1000000007
N = int(input())
A = list(map(int, input().split()))
base = 1
result = 0
for i in range(N):
    result = (result + base * A[i]) % MOD
    base = (base << 1) % MOD
print(result)
