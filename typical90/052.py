N = int(input())
MOD = 10**9 + 7
result = 1
for n in range(N):
    result = (result * (sum([int(l) for l in input().split()]) % MOD )) % MOD
print(result)
