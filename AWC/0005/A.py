N, K = map(int, input().split())
P = [int(l) for l in input().split()]
result = 0
for p in P:
    result += p if p % K == 0 else 0
print(result)
