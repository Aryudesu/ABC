N, M = map(int, input().split())
A = list(map(int, input().split()))
result = M
for a in A:
    result = (result * a) // 100
print(result)
