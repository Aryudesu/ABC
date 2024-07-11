N, L = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = 0
for a in A:
    if a >= L:
        result += 1
print(result)
