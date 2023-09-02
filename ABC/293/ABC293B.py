N = int(input())
A = [int(l) for l in input().split()]
person = [False] * (N + 1)
for idx in range(1, N + 1):
    p = A[idx - 1]
    if not person[idx]:
        person[p] = True
result = []
for idx in range(1, N + 1):
    if not person[idx]:
        result.append(idx)
print(len(result))
print(*result)
