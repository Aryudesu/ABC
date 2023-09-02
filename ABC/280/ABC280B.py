N = int(input())
S = [int(l) for l in input().split()]
result = []
prev = 0
for s in S:
    result.append(s - prev)
    prev = s
print(*result)
