N, T = map(int, input().split())
result = 0
for n in range(N):
    a, c = map(int, input().split())
    if T > a:
        result += (T - a) * c
print(result)
