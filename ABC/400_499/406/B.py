N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = 1
for a in A:
    result *= a
    if len(str(result)) > K:
        result = 1
print(result)

