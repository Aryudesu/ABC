N, M = map(int, input().split())
data = set()
result = 0
for m in range(M):
    a, b = map(int, input().split())
    if (a, b) in data:
        result += 1
    data.add((a, b))
    data.add((b, a))
print(result)
