N, S = [int(l) for l in input().split()]
result = 0
for n in range(1, N+1):
    for m in range(1, N+1):
        if(n + m) <= S:
            result += 1
print(result)
