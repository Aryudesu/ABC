N = int(input())
data = [0] * N
for n in range(N):
    x, y = map(int, input().split())
    data[y-1] = x
minX = N + 5
result = 0
for y in range(N):
    x = data[y]
    if x < minX:
        result += 1
        minX = x
print(result)
