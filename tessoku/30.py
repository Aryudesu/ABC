MOD = 1000000007
N, R = [int(l) for l in input().split()]
R = N - R if R > N - R else R
result = 1
count = 1
for n in range(N - R + 1, N + 1):
    result *= n
    while result % count == 0 and count <= N - R:
        result = result // count
        count += 1
print(result % MOD)
