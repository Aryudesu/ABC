N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
A.sort()
B.sort()
result = 0
idx = 0
for a in A:
    if a >= B[idx]:
        result += a
        idx += 1
    if idx >= M:
        break
print(result if idx >= M else "-1")
