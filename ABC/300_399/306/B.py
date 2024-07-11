A = [int(l) for l in input().split()]
base = 1
result = 0
for a in A:
    result += a * base
    base *= 2
print(result)
