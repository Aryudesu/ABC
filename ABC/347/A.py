N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = []
for a in A:
    if a % K == 0:
        result.append(a // K)
print(*result)
