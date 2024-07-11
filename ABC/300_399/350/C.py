N = int(input())
A = [int(l) - 1 for l in input().split()]
data = dict()
for idx in range(N):
    data[A[idx]] = idx
result = []
for idx in range(N):
    if idx == A[idx]:
        continue
    a = A[idx]
    b = data[idx]
    result.append((idx + 1, b + 1))
    A[idx], A[b] = A[b], A[idx]
    data[idx], data[a] = data[a], data[idx]
print(len(result))
for r in result:
    print(*r)
