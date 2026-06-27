N = int(input())
result = 0
sc = 0
for n in range(N):
    a, b = map(int, input().split())
    if a + b > sc:
        sc = a + b
        result = n + 1
print(result)
