N = int(input())
data = [0] * (N + 1)
for y in range(2, N + 1):
    for x in range(1, y):
        n = x * x + y * y
        if n <= N:
            data[n] += 1
        else:
            break
result = []
for i in range(N + 1):
    if data[i] == 1:
        result.append(i)
print(len(result))
print(*result)

