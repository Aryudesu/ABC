N = int(input())
S = input()
MOD = 10**9 + 7
data = []
count = 0
result = 1
for idx in range(N - 2):
    if S[idx] == S[idx + 2] and S[idx] != S[idx + 1]:
        count += 1
    else:
        if count:
            tmp = (count + 1) // 2 + 1
            result = (result * tmp) % MOD
        count = 0
tmp = (count + 1) // 2 + 1
result = (result * tmp) % MOD
print(result)
