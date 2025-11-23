N, P = map(int, input().split())
A = list(map(int, input().split()))
result = 0
for a in A:
    if a < P:
        result += 1
print(result)
