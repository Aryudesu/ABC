N, X = [int(l) for l in input().split()]
result = 0
for a in range(1, N+1):
    for b in range(a+1, N+1):
        c = X - a - b
        if c <= N and a < b < c:
            result += 1
print(result)
