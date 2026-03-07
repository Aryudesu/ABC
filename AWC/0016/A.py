N = int(input())
result = 0
count = 0
for n in range(N):
    a, b = map(int, input().split())
    if a > b:
        result += a - b
        count += 1
print(count, result)
