N, R = map(int, input().split())
result = 0
for n in range(N):
    x, y, p, q = map(int, input().split())
    if (x-p)**2 + (y-q)**2 <= R**2:
        result += 1
print(result)
